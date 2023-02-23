from fastapi import APIRouter
from api.station_location import get_spe_stn_list, get_cur_stn_list
from db.get.db_data import get_stn_name

router = APIRouter(prefix="/bus-api")


# 특정 지역 인근 정류소
@router.get('/stn-info/specific', tags=["인근 정류소"])
def specific_gps_stn(address, rad):
    result = get_spe_stn_list(address, rad)
    return result


# 현재 위치 기반 인근 정류소
@router.get('/stn-info/current', tags=["인근 정류소"])
def current_gps_stn(rad):
    result = get_cur_stn_list(rad)
    return result


# 정류소 데이터 조회
@router.get('/stn-info/stn', tags=["정류소 조회"])
def stn_data(stn_name):
    result = get_stn_name(stn_name)
    return result
