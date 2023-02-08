from fastapi import APIRouter
from db.get_db_data import get_route_list

router = APIRouter(prefix="/bus-api")


# 버스 노선 검색
@router.get('/route-info/{routeNm}', tags=["버스 노선 검색"])
def route_list(routeNm):
    result = get_route_list(routeNm)
    return result
