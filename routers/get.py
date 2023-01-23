from fastapi import APIRouter
from api.api_stn_info import get_station_list, get_cur_stn_list
from api.api_bus_info import get_arrive_bus_info

router = APIRouter()

# 특정 지역 인근 정류소
@router.get("/gps/{stn}")
def read_gps(address: str, rad: int):
    result = get_station_list(address, rad)
    return result

# 현재 위치 기반 인근 정류소
@router.get("/gps/{cur-stn}")
def read_gps(rad: int):
    result = get_cur_stn_list(rad)
    return result


# 정류소에 도착예정인 버스조회
@router.get("/bus-info")
def read_bus_info(stnNm: str, stnId: int):
    result = get_arrive_bus_info(stnNm, stnId)
    return result
