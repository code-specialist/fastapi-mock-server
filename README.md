# FastAPI Mock Server Generator

Creates a mock server from an OpenAPI specification. The examples defined in the definition will be used as mock data. See [https://fastapi.tiangolo.
com/tutorial/schema-extra-example/](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)

e. g.

```python
class WriteCat(BaseModel):
    name: str
    age: int
    breed: str
    food_type: CatFoodType

    class Config:
        schema_extra = {
            "example": {
                "name": "Garfield",
                "age": 3,
                "breed": "Tabby",
                "food_type": CatFoodType.dry,
            }
        }
	    
@app.post("/cats", status_code=201, response_model=Cat)
def create_cat(cat: WriteCat):
    """ Creates a new cat """
    cat = Cat(id=len(cat_list.cats), **cat.dict())
    cat_list.cats.append(cat)
    return cat
```

as a route on the original app will return

```json
{
  "name": "Garfield",
  "age": 3,
  "breed": "Tabby",
  "food_type": "dry"
}
```
on `POST /cats` on the mock server.

This is especially useful for testing and local development.

## Usage

Generate and run a mock server from an OpenAPI specification:

```python
import uvicorn

from source.app_generator import generate_app

app = generate_app("http://localhost:8071/openapi.json")

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8080)
```

**Example output**

```shell
Loading openAPI definition from http://localhost:8071/openapi.json
Generating endpoint GET /cats
Generating endpoint POST /cats
Generating endpoint GET /cats/{cat_id}
Mock server for "Cat App" has been generated
INFO:     Started server process [53349]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```