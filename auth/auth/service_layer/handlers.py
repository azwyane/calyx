from auth.adapters import respository
from auth.domain import model
class AuthenticationService:

    def __init__(self,repo):
        self.repo = repo

    def authenticate_credentials(self,credential:model.CredentialModel):
        return True #suppose credentials are valid