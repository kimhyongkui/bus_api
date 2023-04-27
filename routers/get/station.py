from fastapi import APIRouter, status
from api.station_location import get_spe_stn_list, get_cur_stn_list
from db.get.db_data import get_stn_name

router = APIRouter(prefix="/stn-data")


# 특정 지역 인근 정류소
@router.get('/specific/{address}', tags=["인근 정류소"])
def specific_gps_stn(address: str, rad: int):
    result = get_spe_stn_list(address, rad)
    return result


# 현재 위치 기반 인근 정류소
@router.get('/current', tags=["인근 정류소"])
def current_gps_stn(rad: int):
    result = get_cur_stn_list(rad)
    return result


# 정류소 데이터 조회
@router.get('/{stn_name}', tags=["정류소 조회"])
def stn_data(stn_name: str):
    result = get_stn_name(stn_name)
    return result
