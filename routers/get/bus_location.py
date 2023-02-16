from fastapi import APIRouter
from api.vehicle import get_bus_info

router = APIRouter(prefix="/bus-api")


# 특정 노선 실시간 버스 위치
@router.get('/bus-location/{routeNm}', tags=["실시간 버스 위치 조회"])
def realtime_bus_loc(routeNm):
    try:
        result = get_bus_info(routeNm)
        return result
    except:
        return '노선명을 다시 확인해주세요'
