from fastapi import FastAPI
from typing import List
from db import session
from models import RouteTable, Route, StationTable, Station

app = FastAPI()


@app.get("/routes")
def read_routes():
    routes = session.query(RouteTable).all()
    return routes

@app.get("/stations")
def read_stations():
    stations = session.query(StationTable).all()
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

