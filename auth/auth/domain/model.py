from pydantic import BaseModel
from auth.domain import command
class CredentialModel(BaseModel):
    unique_id: str
    pin: str


def credential_factory(authenticate_command: command.AuthenticateUserCommand):
    return CredentialModel(
        unique_id=authenticate_command.username,
        pin=authenticate_command.password
    )