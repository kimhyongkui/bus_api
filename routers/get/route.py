from fastapi import APIRouter
from db.get.db_data import get_route_list

router = APIRouter(prefix="/bus-api")


# 버스 노선 검색
@router.get('/route-info', tags=["버스 노선 검색"])
def route_list(route_name):
    result = get_route_list(route_name)
    return result
