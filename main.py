from routers import get, post, patch, delete
from fastapi import FastAPI

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(patch.router)
app.include_router(delete.router)
