from fastapi import APIRouter
from api.api_stn_info import get_station_list, get_cur_stn_list
from api.api_bus_info import get_arrive_bus_info
from api.api_vehicle import get_bus_info
from db.db_get_data import get_stn_name, get_route_list


router = APIRouter(prefix="/bus-api")


# 특정 지역 인근 정류소
@router.get('/gps/{address}', tags=["인근 정류소"])
def specific_stn_gps(address, rad):
    result = get_station_list(address, rad)
    return result


# 현재 위치 기반 인근 정류소
@router.get('/gps/cur-stn', tags=["인근 정류소"])
def cur_stn_gps(rad):
    result = get_cur_stn_list(rad)
    return result


# 정류소 데이터 조회
@router.get('/stn-info', tags=["정류소 조회"])
def stn_info(stnNm):
    result = get_stn_name(stnNm)
    return result


# 정류소에 도착예정인 버스조회
@router.get('/arrive-bus-info', tags=["도착 예정 버스 조회"])
def arrive_bus_info(stnNm, stnId):
    result = get_arrive_bus_info(stnNm, stnId)
    return result


# 버스 노선 검색
@router.get('/route-info', tags=["버스 노선 검색"])
def route_list(routeNm):
    result = get_route_list(routeNm)
    return result


# 특정 노선 실시간 버스 위치
@router.get('/bus-location', tags=["실시간 버스 위치 조회"])
def rt_bus_loc(routeNm):
    result = get_bus_info(routeNm)
    return result

