from fastapi import APIRouter
from api.stn_info import get_station_list, get_cur_stn_list
from db.get.db_data import get_stn_name

router = APIRouter(prefix="/bus-api")


# 특정 지역 인근 정류소
@router.get('/stn-info/{address}', tags=["인근 정류소"])
def specific_stn_gps(address, rad):
    if get_station_list(address, rad) == 'Null':
        return {"주소와 거리 다시 입력"}
    else:
        result = get_station_list(address, rad)
        return result


# 현재 위치 기반 인근 정류소
@router.get('/stn-info/cur-stn', tags=["인근 정류소"])
def current_stn_gps(rad):
    if get_cur_stn_list(rad) == 'Null':
        return {"틀림"}
    else:
        result = get_cur_stn_list(rad)
        return result


# 정류소 데이터 조회
@router.get('/stn-info/{stnNm}', tags=["정류소 조회"])
def stn_info(stnNm: str):
    if get_stn_name(stnNm) == ():
        return {"정류소이름 다시 입력"}
    else:
        result = get_stn_name(stnNm)
        return result
