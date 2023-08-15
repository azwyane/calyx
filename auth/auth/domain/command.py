from pydantic import BaseModel

class AbstractCommand(BaseModel):
    pass

class AuthenticateUserCommand(AbstractCommand):
    username: str
    password: str