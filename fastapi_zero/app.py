from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.scheme import MessageSchema, UserPublicSchema, UserSchema

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'Hello World!'}


@app.post("/users", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def read_root(user: UserSchema):
    return user
