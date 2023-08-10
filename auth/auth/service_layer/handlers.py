from auth.domain import command, model

def self_indentification():
    payload = {
            "id" : 1,
            "name" : "azwyane",
            "age"  : 22
        }
    user = model.User(**payload)
    return user

def register_user(user):
    # TODO
    # user = respository.UserRespository.save(user)
    return user
    

