from abc import ABC, abstractmethod
from auth.domain import model
class AbstractRepository(ABC):
    
    @abstractmethod
    def get(self,id):
        pass

    @abstractmethod
    def add(self,user:model.User):
        pass

    @abstractmethod
    def update(self,user:model.User):
        pass

class FakeUserRepository(AbstractRepository):
    
    def __init__(self):
        self.db = [
                    {
                        "id" : 1,
                        "name" : "azwyane",
                        "age"  : 22
                    }
                ]

    def get(self,id):
        for user in self.db:
            if user["id"] == id:
                return model.User(**user)
        else:
            return None

    def add(self,user:model.User):
        self.db.append(user)
        return user

    def update(self,user:model.User):
        self.db.append(user)
        return user
class UserRespository():
    pass
