from fastapi import APIRouter, status
from api.arrival_bus_info import get_arrival_buses

router = APIRouter(prefix="/arrival")


# 정류소에 도착예정인 버스조회
@router.get('/buses/{stn_name}', tags=["도착 예정 버스 조회"])
def arrival_buses(stn_name: str, stn_id: int):
    result = get_arrival_buses(stn_name, stn_id)
    return result
