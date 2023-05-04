from fastapi import APIRouter, Depends
from db.post.vehicle_data import add_veh_data, add_all_veh_data
from app.auth import get_admin

router = APIRouter(prefix="/vehicle")


@router.post('/route_data', tags=["버스"], dependencies=[Depends(get_admin)])
def vehicle_data(route_name):
    result = add_veh_data(route_name)
    return result


@router.post('/route_data/all', tags=["버스"], dependencies=[Depends(get_admin)])
def all_vehicle_data():
    result = add_all_veh_data()
    return result