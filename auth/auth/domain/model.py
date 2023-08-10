from pydantic import BaseModel

class AbstractDomain(BaseModel):
    pass

class User(AbstractDomain):
    id: int
    name: str
    age: int 

    def capitalize_name(self):
        self.name = self.name.capitalize()
        return

def user_registration_factory(command):
    user = User(
            id=command.id,
            name=command.name,
            age=command.age
            )
    return user
