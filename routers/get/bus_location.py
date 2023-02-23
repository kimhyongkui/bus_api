from fastapi import APIRouter
from api.vehicle import get_vehicle_data

router = APIRouter(prefix="/bus-api")


# 특정 노선 실시간 버스 위치
@router.get('/bus-location', tags=["실시간 버스 위치 조회"])
def realtime_bus_loc(route_name):
    result = get_vehicle_data(route_name)
    return result
