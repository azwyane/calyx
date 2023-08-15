from fastapi import FastAPI
from identity.entrypoints.views import router

app = FastAPI()

app.include_router(router)
