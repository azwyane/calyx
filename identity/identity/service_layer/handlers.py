from identity.domain import model

class UserService:
    
    def __init__(self,repo):
        self.repo = repo

    def indentification(self,id):
        user = self.repo.get(id=id)
        return user

    def register_user(self,user: model.User):
        user = self.repo.add(user)
        return user

    def capitalize_user(self,user:model.User):
        user.capitalize_name()
        user = self.repo.update(user)
        return user




