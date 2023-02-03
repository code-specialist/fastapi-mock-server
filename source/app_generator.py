from fastapi import FastAPI

from source.endpoints import router
from source.endpoints_generator import parse_open_api


def generate_mock_app(open_api_url: str, ignore: list[str], proxy_path: str ="/") -> FastAPI:
    """ Generates a FastAPI app with the endpoints from the router and the openapi schema from the openapi_url """
    open_api_schema = parse_open_api(open_api_url=open_api_url, ignore=ignore, proxy_path=proxy_path)
    generated_app = FastAPI()
    generated_app.openapi_schema = open_api_schema
    generated_app.include_router(router)
    print(f'Mock server for "{generated_app.title}" has been generated') # TODO: Use logger
    return generated_app
