from pydantic import BaseModel
import random
class AbstractEntity(BaseModel):
    pass

class UserResponse(AbstractEntity):
    id: int 
    username: str
    email: str 
class User(AbstractEntity):
    id: int 
    username: str
    email: str 
    password: str

    def capitalize_name(self):
        self.username = self.username.capitalize()
        return

def user_registration_factory(command):
    user = User(
            id = random.randint(1,10000),
            username=command.user.username,
            email=command.user.email,
            password=command.credentials.password1
            )
    return user
