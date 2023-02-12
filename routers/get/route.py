from fastapi import APIRouter
from db.get.db_data import get_route_list

router = APIRouter(prefix="/bus-api")


# 버스 노선 검색
@router.get('/route-info/{routeNm}', tags=["버스 노선 검색"])
def route_list(routeNm):
    try:
        if get_route_list(routeNm) != ():
            result = get_route_list(routeNm)
            return result
    except:
        return '노선명을 다시 입력하세요'
