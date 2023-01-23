from routers import get, post, update, delete
from fastapi import FastAPI

app = FastAPI()

app.include_router(get.router)
app.include_router(post.router)
app.include_router(update.router)
app.include_router(delete.router)


