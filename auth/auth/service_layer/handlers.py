from auth.domain import model
from auth.adapters import respository
class UserService:
    
    def __init__(self):
        self.repo = respository.FakeUserRepository()

    def indentification(self,id):
        user = self.repo.get(id=id)
        return user

    def register_user(self,user: model.User):
        user = self.repo.add(user)
        return user

    def capitalize_user(self,user:model.User):
        user = self.repo.get(id=id)
        if user:
            user.capitalize_name()
            user = self.repo.update(user)
        return user


class UserAuthenticationService:
    pass


