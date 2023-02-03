import json
import os
import pathlib
from enum import Enum
from urllib import request

from jinja2 import Environment, FileSystemLoader
from openapi_schema_pydantic import OpenAPI, Operation as OpenAPIOperation, Schema as OpenAPISchema, Reference as OpenAPIReference, Parameter as OpenAPIParameter
from pydantic.main import BaseModel

supported_methods = ["get", "post", "put", "delete"]
current_path = pathlib.Path(__file__).parent.absolute()
templates_path = os.path.join(current_path, "templates")
endpoints_path = os.path.join(current_path, "endpoints.py")
jinja_loader = FileSystemLoader(templates_path)
# noinspection JinjaAutoinspect
environment = Environment(loader=jinja_loader)


class ParameterType(Enum):
    """ Represents the type of a parameter. With the corresponding Python type."""
    str = "string"
    int = "integer"
    float = "number"
    bool = "boolean"
    list = "array"
    dict = "object"
    enum = "enum"


class Parameter(BaseModel):
    """ Represents a parameter. DTO. """
    name: str
    required: bool
    type: ParameterType
    default: str | None  # TODO: Use fancy type evaluation to get the correct type for things like bools and ints


class Endpoint(BaseModel):
    """ Represents an endpoint. DTO. """
    name: str
    path: str
    method: str
    response: dict
    parameters: list[Parameter]


def _get_schema(response_model_name: str, open_api) -> OpenAPISchema | None:
    """ Returns the schema for the given response model name """
    if response_model_name is None:
        return None
    return open_api.components.schemas[response_model_name]


def _get_schema_ref(media_type_schema) -> str:
    """ Returns the schema ref for the given media type schema """
    try:
        return getattr(media_type_schema, "ref")
    except AttributeError:  # Recursion
        return _get_schema_ref(getattr(media_type_schema, "items"))


def _schema_name_from_ref(schema_ref: str) -> str:
    """ Returns the schema name from the given schema ref """
    return schema_ref.split("/")[-1]


def _get_response_model(path_method: OpenAPIOperation) -> str or None:
    """ Returns the response model for the given path method """
    for status_code in range(200, 299):
        try:
            path_response = path_method.responses[str(status_code)]
            content = getattr(path_response, "content")
            json = content["application/json"]
            media_type_schema = getattr(json, "media_type_schema")
            schema_ref = _get_schema_ref(media_type_schema)
            return _schema_name_from_ref(schema_ref)  # '#/components/schemas/CatList' => 'CatList'
        except (KeyError, AttributeError):
            pass
    return None


def _get_parameter_schema(parameter: OpenAPIParameter, open_api: OpenAPI) -> OpenAPISchema:
    if not hasattr(parameter, "param_schema"):
        if hasattr(parameter, "enum"):
            return parameter
    if not type(parameter.param_schema) == OpenAPIReference:
        return parameter.param_schema
    schema_ref = _get_schema_ref(parameter.param_schema)
    schema_name = _schema_name_from_ref(schema_ref)
    schema = _get_schema(schema_name, open_api)
    return _get_parameter_schema(schema, open_api)


def load_open_api(openapi_url: str) -> dict:
    """ Loads the openapi schema from the given url """
    with request.urlopen(openapi_url) as response:
        return json.loads(response.read().decode())


def parse_open_api(open_api_url: str, ignore: list[str], proxy_path: str):
    """ Generates the endpoints.py file from the openapi schema """

    print(f"Loading openAPI definition from {open_api_url}")  # TODO: Use logger

    open_api_json = load_open_api(open_api_url)
    open_api = OpenAPI.parse_obj(open_api_json)
    open_api_json["info"]["title"] = f"{open_api_json['info']['title']} Mock Server"
    open_api_json["info"]["description"] = f"This is an auto-generated mock server for {open_api_json['info']['title']}."
    open_api_json["servers"] = [{"url": proxy_path}]

    template = environment.get_template("endpoints.jinja")
    endpoints = []

    # Iterate over paths
    for path in open_api.paths:
        path_options = open_api.paths[path]

        # Skip if path is in ignore list
        if path in ignore:
            del open_api_json["paths"][path]  # Remove path from openapi schema
            continue

        # Iterate over supported methods
        for method in supported_methods:
            path_method: OpenAPIOperation = getattr(path_options, method, None)

            # If method is supported
            if path_method is not None:
                response_model_name: str = _get_response_model(path_method)
                schema: OpenAPISchema = _get_schema(response_model_name, open_api)

                if not schema:
                    print(f"Could not find schema for {method.upper()} {path}. Skipping")  # TODO: Use logger
                    del open_api_json["paths"][path][method]  # Remove method from openapi schema
                    continue

                example: dict = schema.example
                print(f"Generating endpoint {method.upper()} {path}")  # TODO: Use logger

                # If the method has parameters
                if path_method.parameters:
                    parameters = []
                    for parameter in path_method.parameters:
                        parameter_schema = _get_parameter_schema(parameter, open_api)
                        parameter_schema_type = ParameterType(parameter_schema.type)
                        try:
                            default = parameter_schema.default
                        except AttributeError:
                            default = None

                        parameters.append(
                            Parameter(
                                name=parameter.name,
                                required=parameter.required,
                                type=parameter_schema_type,
                                default=default
                            ))
                else:
                    parameters = []

                # If the method has no example
                if not example:
                    print(f"Could not find example for {method.upper()} {path}. Skipping.")
                    del open_api_json["paths"][path][method]  # Remove method from openapi schema
                    continue

                endpoints.append(
                    Endpoint(
                        path=path,
                        method=method,
                        response=example,
                        name=path_method.operationId,
                        parameters=parameters
                    )
                )

    template_rendering = template.render(endpoints=endpoints)
    open(endpoints_path, "w+").write(template_rendering)
    return open_api_json  # Return the openapi schema with altered paths
