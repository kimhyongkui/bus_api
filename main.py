import os
from dotenv import load_dotenv
from api.routers.get import bus_location, station, route, arrive_bus
from api.routers.post import route_data, join, login, station_data, vehicle, route_list
from fastapi import FastAPI
import uvicorn

load_dotenv()

app = FastAPI(title="서울시 버스 정보 조회")

# get
app.include_router(station.router, prefix="/bus-api")
app.include_router(arrive_bus.router, prefix="/bus-api")
app.include_router(route.router, prefix="/bus-api")
app.include_router(bus_location.router, prefix="/bus-api")
# post
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
        port = 8080
    else:
        # 배포 환경 설정
        host = os.getenv("SERVER_HOST")
        port = int(os.getenv("SERVER_PORT"))

    # FastAPI 실행
    uvicorn.run("main:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    main()
