from pydantic import BaseModel


class AbstractCommand(BaseModel):
    pass

class RegisterUserCommand(AbstractCommand):
    id: int
    name: str
    age: int 