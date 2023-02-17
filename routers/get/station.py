from fastapi import APIRouter
from api.stn_info import get_station_list, get_cur_stn_list
from db.get.db_data import get_stn_name

router = APIRouter(prefix="/bus-api")


# 특정 지역 인근 정류소
@router.get('/stn-info/specific/{address}', tags=["인근 정류소"])
def specific_stn_gps(address, rad):
    result = get_station_list(address, rad)
    if get_station_list(address, rad) != 'Null':
        return result
    else:
        return '주소와 거리 다시 입력'


# 현재 위치 기반 인근 정류소
@router.get('/stn-info/current/stn', tags=["인근 정류소"])
def current_stn_gps(rad):
    result = get_cur_stn_list(rad)
    if get_cur_stn_list(rad) != 'Null':
        return result
    else:
        return '거리 내에 정류소가 없습니다.'


# 정류소 데이터 조회
@router.get('/stn-info/{stnNm}', tags=["정류소 조회"])
def stn_info(stnNm: str):
    result = get_stn_name(stnNm)
    if get_stn_name(stnNm):
        return result
    else:
        return '정류소 이름 다시 입력'
