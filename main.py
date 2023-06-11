import os
from dotenv import load_dotenv
from routers.get import station, arrive_bus, bus_location, route
from routers.post import route_data, route_list, station_data, vehicle, join, login
from fastapi import FastAPI
import uvicorn

load_dotenv()

app = FastAPI(title="bus_api")

app.include_router(station.router, prefix="/bus-api")
app.include_router(arrive_bus.router, prefix="/bus-api")
app.include_router(route.router, prefix="/bus-api")
app.include_router(bus_location.router, prefix="/bus-api")

app.include_router(route_data.router, prefix="/bus-api")
app.include_router(route_list.router, prefix="/bus-api")
app.include_router(station_data.router, prefix="/bus-api")
app.include_router(vehicle.router, prefix="/bus-api")
app.include_router(join.router, prefix="/bus-api")
app.include_router(login.router, prefix="/bus-api")


def main():
    environment = os.getenv("ENVIRONMENT")
    if environment == "local":
        # 로컬 환경 설정
        host = "localhost"
        port = 8000
    else:
        # 배포 환경 설정
        host = os.getenv("SERVER_HOST")
        port = int(os.getenv("SERVER_PORT"))

    # FastAPI 실행
    uvicorn.run("main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()
