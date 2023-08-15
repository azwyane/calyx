from fastapi import APIRouter, HTTPException

from identity.domain import command, model
from identity.service_layer import handlers
from identity.adapters import respository

router = APIRouter()

repo = respository.FakeUserRepository()
user_service = handlers.UserService(repo=repo)

@router.get("/user/")
def view_user():
    #TODO get bearer token and validate -> authorized() -> return user instance
    # get user id from user instance

    user = user_service.indentification(id=1) #pass id = user.id
    return user

@router.post("/user/") 
def create_user(registercommand:command.RegisterUserCommand):
    user_model = model.user_registration_factory(registercommand)
    user_id_db = repo.get_by_email(email=user_model.email)
    if user_id_db:
        raise HTTPException(status_code=409, detail="User already exists with provided email")
    user = user_service.register_user(user_model)
    return user
    

@router.put("/user/update/") #get method just for demo
def update_user():
    payload = {
        "id" : 1,
        "name" : "azwyane",
        "age"  : 22
    }
    registercommand = command.RegisterUserCommand(**payload)
    user_model = model.user_registration_factory(registercommand)
    user = user_service.capitalize_user(user_model)
    return user


