from fastapi import APIRouter, status, HTTPException
from api.station_location import get_spe_stn_list, get_cur_stn_list
from db.get.db_data import get_stn_name

router = APIRouter(prefix="/stn-data")


# 특정 지역 인근 정류소
@router.get('/specific/{address}', tags=["인근 정류소"], status_code=status.HTTP_200_OK)
def specific_gps_stn(address: str, rad: int):
    try:
        result = get_spe_stn_list(address, rad)
        return result

    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="에러 발생")


# 현재 위치 기반 인근 정류소
@router.get('/current', tags=["인근 정류소"], status_code=status.HTTP_200_OK)
def current_gps_stn(rad: int):
    try:
        result = get_cur_stn_list(rad)
        return result

    except TimeoutError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="geoplugin 접속 오류")

    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="에러 발생")


# 정류소 데이터 조회
@router.get('/{stn_name}', tags=["정류소 조회"], status_code=status.HTTP_200_OK)
def stn_data(stn_name: str):
    try:
        result = get_stn_name(stn_name)
        return result

    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="에러 발생")
