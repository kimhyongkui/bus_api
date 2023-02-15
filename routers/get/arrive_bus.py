from fastapi import APIRouter
from api.bus_info import get_arrive_bus_info

router = APIRouter(prefix="/bus-api")


# 정류소에 도착예정인 버스조회
@router.get('/arrive-bus-info/{stnNm}', tags=["도착 예정 버스 조회"])
def arrive_bus_info(stnNm, stnId):
    try:
        result = get_arrive_bus_info(stnNm, stnId)
        return result
    except:
        return '정류소 이름과 ID를 확인하세요'