from fastapi import APIRouter
from api.api_stn_info import get_station_list, get_cur_stn_list
from api.api_bus_info import get_arrive_bus_info
from api.api_station import get_station
from api.api_vehicle import get_bus_info

router = APIRouter()


# 특정 지역 인근 정류소
@router.get("/gps/{stn}")
def get_gps(address: str, rad: int):
    result = get_station_list(address, rad)
    return result


# 현재 위치 기반 인근 정류소
@router.get("/gps/{cur-stn}")
def get_gps(rad: int):
    result = get_cur_stn_list(rad)
    return result


# 정류소에 도착예정인 버스조회
@router.get("/bus-info")
def get_arrive_bus(stnNm: str, stnId: int):
    result = get_arrive_bus_info(stnNm, stnId)
    return result


# 버스 노선 검색
@router.get("/route-info")
def get_route_info(routeId):
    # 버스 노선을 입력하면 해당 노선의 리스트를 띄워줌
    result = get_station(routeId)
    stn_list = []
    for i in result:
        stnNm = i['stnNm']
        stn_list.append(stnNm)
    return stn_list



# 특정 노선 실시간 버스 위치
@router.get("/bus-location")
def get_bus_location(routeId):
    # 버스 노선을 입력하면 해당 노선의 리스트를 띄워줌
    result = get_bus_info(routeId)
    return result
