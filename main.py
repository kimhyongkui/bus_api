from routers.get import station, arrive_bus, bus_location, route
from fastapi import FastAPI


app = FastAPI(title="bus_api")

app.include_router(station.router, prefix="/bus_api")
app.include_router(arrive_bus.router, prefix="/bus_api")
app.include_router(route.router, prefix="/bus_api")
app.include_router(bus_location.router, prefix="/bus_api")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        reload=True,
        port=8000)
