from fastapi import FastAPI
from typing import List
from db import session
from models import RouteTable, Route, StationTable
from api_gps import get_station_list
from api_bus_info import get_arrive_bus_info


app = FastAPI()


@app.get("/gps")
def read_gps(address: str, rad: int):
    result = get_station_list(address, rad)
    return result

@app.get("/bus-info")
def read_bus_info(stnNm: str, stnId: int):
    result = get_arrive_bus_info(stnNm, stnId)
    return result


@app.get("/routes")
def read_routes():
    routes = session.query(RouteTable).all()
    return routes


@app.get("/stations/{stationid}")
def read_stations(routeId: int):
    stations = session.query(StationTable).filter(StationTable.routeId == routeId).first()
    return stations


@app.get("/routes/{routeid}")
def read_route(routeId: int):
    route = session.query(RouteTable).filter(RouteTable.routeId == routeId).first()
    return route


@app.post("/route")
def create_route(routeNm: str, routeAbrv: str, routeId: int):
    route = RouteTable()
    route.routeNm = routeNm
    route.routeAbrv = routeAbrv
    route.routeId = routeId

    session.add(route)
    session.commit()

    return f"{routeNm} created..."


@app.put("/routes")
def update_route(routes: List[Route]):
    for i in routes:
        route = session.query(RouteTable).filter(RouteTable.no == i.no).first()
        route.routeNm = i.routeNm
        route.routeAbrv = i.routeAbrv
        route.routeId = i.routeId
        session.commit()

    return f"{i.routeNm} updated..."


@app.delete("/route")
def delete_rotue(routeId: int):
    route = session.query(RouteTable).filter(RouteTable.routeId == routeId).delete()
    session.commit()

    return f"{routeId} deleted..."










