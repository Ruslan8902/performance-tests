from pydantic import BaseModel, Field, HttpUrl, EmailStr, ValidationError


class UserSchema(BaseModel):
    """
        Модель данных пользователя
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserRequestSchema(BaseModel):
    """
        Модель данных запроса на создание пользователя
    """
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    phone_number: str = Field(alias='phoneNumber')


class CreateUserResponse(BaseModel):
    """
        Модель данных ответа с данными созданного пользователя
    """
    user: UserSchema
