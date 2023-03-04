from fastapi import APIRouter
from db.get.db_data import get_route_data

router = APIRouter(prefix="/route")


# 버스 노선 검색
@router.get('/route_data/{route_name}', tags=["버스 노선 검색"])
def route_data(route_name: str):
    result = get_route_data(route_name)
    return result
