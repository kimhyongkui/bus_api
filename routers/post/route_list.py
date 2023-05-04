from fastapi import APIRouter, Depends
from db.post.route_list import add_route_list
from app.auth import get_admin

router = APIRouter(prefix="/route")


@router.post('/route_list', tags=["노선"], dependencies=[Depends(get_admin)])
def route_list():
    result = add_route_list()
    return result
