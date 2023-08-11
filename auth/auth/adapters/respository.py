from abc import ABC, abstractmethod
from auth.domain import model

class AbstractRepository(ABC):
    
    @abstractmethod
    def get(self,id):
        raise NotImplementedError

    @abstractmethod
    def add(self,user:model.User):
        raise NotImplementedError

    @abstractmethod
    def update(self,user:model.User):
        raise NotImplementedError

class FakeUserRepository(AbstractRepository):
    
    def __init__(self):
        self.db = [
                    {
                        "id" : 1,
                        "username" : "azwyane",
                        "email"  : "iexist.com",
                        "password": "mypassword"
                    }
                ]

    def get(self,id):
        for user in self.db:
            if user["id"] == id:
                return model.UserResponse(**user)
        else:
            return None

    def add(self,user:model.User):
        self.db.append(user)
        return model.UserResponse(**user.dict())

    def update(self,user:model.User):
        self.db.append(user)
        return model.UserResponse(**user.dict())

    def get_by_email(self,email):
        for user in self.db:
            if user['email'] == email:
                return model.UserResponse(**user)
        else:
            return None
class UserRespository():
    pass
