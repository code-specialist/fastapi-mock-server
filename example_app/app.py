import uvicorn
from fastapi import FastAPI
from fastapi.responses import Response
from example_app.model import Cat, WriteCat, CatList

app = FastAPI(
    title="Cat App",
    description="This is a very fancy project, with auto docs for the API and everything",
    version="1.0.0"
)

cat_list: CatList = CatList(cats=[])


@app.get("/cats", response_model=CatList)
def read_cats(odd_only: bool = False):
    """ Returns a list of all cats """
    if odd_only:
        return CatList(cats=[cat for cat in cat_list.cats if cat.id % 2 == 1])
    return cat_list


@app.post("/cats", status_code=201, response_model=Cat)
def create_cat(cat: WriteCat):
    """ Creates a new cat """
    cat = Cat(id=len(cat_list.cats), **cat.dict())
    cat_list.cats.append(cat)
    return cat


@app.get("/cats/{cat_id}", response_model=Cat)
def read_cat(cat_id: int, some_param: str = "some_default"):
    """ Returns a single cat by ID """
    if cat_id >= len(cat_list.cats) or cat_id < 0:
        return Response(status_code=404, content="Cat not found")
    return cat_list.cats[cat_id]


if __name__ == '__main__':
    uvicorn.run(app=app, port=8071)
