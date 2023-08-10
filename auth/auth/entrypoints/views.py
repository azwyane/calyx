from fastapi import APIRouter

from auth.domain import command, model
from auth.service_layer import handlers

router = APIRouter()

class UserAPIView:

    @router.get("/")
    def view_user():
        user = handlers.self_indentification()
        return user

    @router.get("/create_user") #get method just for demo
    def create_user():
        payload = {
            "id" : 1,
            "name" : "azwyane",
            "age"  : 22
        }
        registercommand = command.RegisterUserCommand(**payload)
        user_model = model.user_registration_factory(registercommand)
        user = handlers.register_user(user_model)
        return user

