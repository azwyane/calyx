from fastapi import APIRouter

from auth.domain import command, model
from auth.service_layer import handlers

router = APIRouter()

user_service = handlers.UserService()

@router.get("/user")
def view_user():
    user = user_service.indentification(id=2)
    return user

@router.get("/user/create/") #get method just for demo
def create_user():
    payload = {
        "id" : 2,
        "name" : "azwyane",
        "age"  : 22
    }
    registercommand = command.RegisterUserCommand(**payload)
    user_model = model.user_registration_factory(registercommand)
    user = user_service.register_user(user_model)
    return user

@router.get("/user/update/") #get method just for demo
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


