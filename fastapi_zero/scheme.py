from pydantic import BaseModel, EmailStr


class MessageSchema(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublicSchema(BaseModel):
    username: str
    email: EmailStr


# class UserListSchema(BaseModel):
#     user = list[UserSchema]
