from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/cats")
async def read_cats_cats_get(odd_only: bool):
    return JSONResponse({'cats': [{'id': 0, 'name': 'Garfield', 'age': 3, 'breed': 'Tabby', 'food_type': 'dry'},
                                  {'id': 1, 'name': 'Felix', 'age': 2, 'breed': 'T-Rex', 'food_type': 'wet'},
                                  {'id': 2, 'name': 'Tom', 'age': 1, 'breed': 'Siamese', 'food_type': 'dry'}]})


@router.post("/cats")
async def create_cat_cats_post():
    return JSONResponse({'id': 0, 'name': 'Garfield', 'age': 3, 'breed': 'Tabby', 'food_type': 'dry'})


@router.get("/cats/{cat_id}")
async def read_cat_cats__cat_id__get(cat_id: int):
    return JSONResponse({'id': 0, 'name': 'Garfield', 'age': 3, 'breed': 'Tabby', 'food_type': 'dry'})
