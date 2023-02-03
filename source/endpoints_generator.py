import json
import os
import pathlib
from enum import Enum
from urllib import request

from jinja2 import Environment, FileSystemLoader
from openapi_schema_pydantic import OpenAPI, Operation, Schema
from pydantic.main import BaseModel

supported_methods = ["get", "post", "put", "delete"]


class ParameterType(Enum):
    """ Represents the type of a parameter. With the corresponding Python type."""
    str = "string"
    int = "integer"
    float = "number"
    bool = "boolean"
    list = "array"
    dict = "object"


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


def _get_schema(response_model_name: str, open_api) -> Schema:
    """ Returns the schema for the given response model name """
    if response_model_name is None:
        return None
    return open_api.components.schemas[response_model_name]


def _get_response_model(path_method: Operation) -> str or None:
    """ Returns the response model for the given path method """
    for status_code in range(200, 299):
        try:
            path_response = path_method.responses[str(status_code)]
            content = getattr(path_response, "content")
            json = content["application/json"]
            media_type_schema = getattr(json, "media_type_schema")
            schema_ref = getattr(media_type_schema, "ref")
            return schema_ref.split("/")[-1]  # '#/components/schemas/CatList' => 'CatList'
        except KeyError:
            pass
    return None


def load_open_api(openapi_url: str) -> dict:
    """ Loads the openapi schema from the given url """
    with request.urlopen(openapi_url) as response:
        return json.loads(response.read().decode())


def generate_endpoints(openapi_url: str):
    """ Generates the endpoints.py file from the openapi schema """
    print(f"Loading openAPI definition from {openapi_url}")  # TODO: Use logger
    open_api_json = load_open_api(openapi_url)
    open_api = OpenAPI.parse_obj(open_api_json)
    templates_path = os.path.join(pathlib.Path(__file__).parent.absolute(), "templates")
    environment = Environment(loader=FileSystemLoader(templates_path))
    template = environment.get_template("endpoints.jinja")

    endpoints = []

    # Iterate over paths
    for path in open_api.paths:
        path_options = open_api.paths[path]

        # Iterate over supported methods
        for method in supported_methods:
            path_method: Operation = getattr(path_options, method, None)

            # If method is supported
            if path_method is not None:
                response_model_name: str = _get_response_model(path_method)
                schema: Schema = _get_schema(response_model_name, open_api)
                example: dict = schema.example
                print(f"Generating endpoint {method.upper()} {path}")  # TODO: Use logger

                if path_method.parameters:
                    parameters = [Parameter(
                        name=parameter.name,
                        required=parameter.required,
                        type=ParameterType(parameter.param_schema.type),
                        default=parameter.param_schema.default
                    ) for parameter in path_method.parameters]
                else:
                    parameters = []
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
    open("endpoints.py", "w").write(template_rendering)
