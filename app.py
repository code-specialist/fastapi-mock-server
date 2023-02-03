import uvicorn

from source.app_generator import generate_mock_app

app = generate_mock_app("http://localhost:5003/openapi.json", ignore=["/health"])

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
