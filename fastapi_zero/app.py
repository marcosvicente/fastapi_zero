from http import HTTPStatus

from fastapi import FastAPI

from fastapi_zero.scheme import MessageSchema, UserPublicSchema, UserSchema

app = FastAPI()

database = []


@app.get("/", status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'Hello World!'}


@app.post("/users", status_code=HTTPStatus.CREATED, response_model=UserPublicSchema)
def create_users(user: UserSchema):
    return user

# @app.get("/users")
# def read_users(response_model=UserListSchema):
#     return { 'users': [] }

@app.put("/users/{user_id}")
def update_users(user_id: int, user: UserSchema):
    return user