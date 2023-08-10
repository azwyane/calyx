from fastapi import FastAPI
from auth.entrypoints.views import router

app = FastAPI()

app.include_router(router)
