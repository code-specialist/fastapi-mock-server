from enum import Enum

from pydantic.main import BaseModel


class CatFoodType(Enum):
    dry = "dry"
    wet = "wet"


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


class Cat(WriteCat):
    id: int

    class Config:
        schema_extra = {
            "example": {
                "id": 0,
                "name": "Garfield",
                "age": 3,
                "breed": "Tabby",
                "food_type": CatFoodType.dry,
            }
        }


class CatList(BaseModel):
    cats: list[Cat]

    class Config:
        schema_extra = {
            "example": {
                "cats": [
                    {
                        "id": 0,
                        "name": "Garfield",
                        "age": 3,
                        "breed": "Tabby",
                        "food_type": CatFoodType.dry,
                    },
                    {
                        "id": 1,
                        "name": "Felix",
                        "age": 2,
                        "breed": "T-Rex",
                        "food_type": CatFoodType.wet,
                    },
                    {
                        "id": 2,
                        "name": "Tom",
                        "age": 1,
                        "breed": "Siamese",
                        "food_type": CatFoodType.dry,
                    }
                ]
            }
        }
