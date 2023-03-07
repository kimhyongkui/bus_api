from routers.get import station, arrive_bus, bus_location, route
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="bus_api")

app.include_router(station.router, prefix="/bus-api")
app.include_router(arrive_bus.router, prefix="/bus-api")
app.include_router(route.router, prefix="/bus-api")
app.include_router(bus_location.router, prefix="/bus-api")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000
    )
