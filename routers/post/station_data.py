from fastapi import APIRouter, Depends
from db.post.station_data import add_station_data, add_all_station_data
from app.auth import get_admin

router = APIRouter(prefix="/station")


@router.post('/route-data', tags=["정류소"], dependencies=[Depends(get_admin)])
def station_data(route_id):
    result = add_station_data(route_id)
    return result


@router.post('/route-data/all', tags=["정류소"], dependencies=[Depends(get_admin)])
def all_station_data():
    result = add_all_station_data()
    return result
