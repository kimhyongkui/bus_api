from routers import get_arrive_bus, get_bus_location, get_stn, get_route, post, patch, delete
from fastapi import FastAPI

app = FastAPI()

app.include_router(get_stn.router)
app.include_router(get_arrive_bus.router)
app.include_router(get_route.router)
app.include_router(get_bus_location.router)

app.include_router(post.router)
app.include_router(patch.router)
app.include_router(delete.router)
