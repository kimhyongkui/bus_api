from fastapi import APIRouter, status, HTTPException
from api.arrival_bus_info import get_arrival_buses

router = APIRouter(prefix="/arrival")


# 정류소에 도착예정인 버스조회
@router.get('/buses/{stn_name}', tags=["도착 예정 버스 조회"], status_code=status.HTTP_200_OK)
def arrival_buses(stn_name: str, stn_id: int):
    try:
        result = get_arrival_buses(stn_name, stn_id)
        return result

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))