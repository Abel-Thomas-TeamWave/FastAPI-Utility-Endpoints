from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="FastAPI Demo App")

app.include_router(router)
