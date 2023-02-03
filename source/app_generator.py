from fastapi import FastAPI

from source.endpoints import router
from source.endpoints_generator import load_open_api, generate_endpoints


def generate_mock_app(open_api_url) -> FastAPI:
    """ Generates a FastAPI app with the endpoints from the router and the openapi schema from the openapi_url """
    generate_endpoints(open_api_url)
    open_api_schema = load_open_api(open_api_url)
    generated_app = FastAPI()
    generated_app.include_router(router)
    generated_app.openapi_schema = open_api_schema
    app_title = open_api_schema["info"]["title"]
    generated_app.title = f"{app_title} Mock Server"
    print(f'Mock server for "{app_title}" has been generated') # TODO: Use logger
    return generated_app
