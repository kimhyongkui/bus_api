from fastapi import APIRouter, Depends
from db.post.route_data import add_route_data, add_all_route_data
from app.auth import get_admin

router = APIRouter(prefix="/route")


@router.post('/route_data', tags=["노선"], dependencies=[Depends(get_admin)])
def route_data(route_id):
    result = add_route_data(route_id)
    return result


@router.post('/route_data/all', tags=["노선"], dependencies=[Depends(get_admin)])
def all_route_data():
    result = add_all_route_data()
    return result
