from fastapi import APIRouter, HTTPException
from auth.domain import command,model
from auth.service_layer import handlers

router = APIRouter()


authentication_service = handlers.AuthenticationService(repo="repo")

@router.post("/auth/")
def authentication(authenticate_command: command.AuthenticateUserCommand):
    credential = model.credential_factory(authenticate_command)
    credential = authentication_service.authenticate_credentials(credential=credential)
    if not credential:
        raise HTTPException(status_code=401,detail="Either username or password provided is wrong")
    return "credential.token, authenticated"