from pydantic import BaseModel, ValidationError, field_validator, Field
from pydantic_core import PydanticCustomError



class AbstractCommand(BaseModel):
    pass
    
class User(AbstractCommand):
    username: str = Field(title="username", max_length=120)
    email: str = Field(title="email", max_length=120)

class Credentials(AbstractCommand):
    password1: str
    password2: str   

    @field_validator('password1','password2')
    @classmethod
    def password_validators(cls, v: str) -> str:
        return v
 
class RegisterUserCommand(AbstractCommand):
    user: User
    credentials: Credentials
