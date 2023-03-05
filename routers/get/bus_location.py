from fastapi import APIRouter, status
from api.vehicle import get_vehicle_data

router = APIRouter(prefix="/bus-location")


# 특정 노선 실시간 버스 위치
@router.get('/realtime/{route_name}', tags=["실시간 버스 위치 조회"], status_code=status.HTTP_200_OK)
def realtime_bus_loc(route_name: str):
    result = get_vehicle_data(route_name)
    return result
