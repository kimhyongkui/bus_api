from routers import get
from fastapi import FastAPI

app = FastAPI()

app.include_router(get.router)


