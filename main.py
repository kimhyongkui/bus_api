from fastapi import FastAPI
from typing import List
from db import session
from models import RouteTable, Route

app = FastAPI()


@app.get("/routes")
def read_routes():
    routes = session.query(RouteTable).all()
    return routes

@app.get("/buses/{bus_id}")
def read_bus(bus_id: int):
    bus = session.query(RouteTable).filter(RouteTable.bus_id == bus_id).first()
    return bus

@app.post("/bus")
def create_bus(bus_name: str, bus_id: int):

    bus = RouteTable()
    bus.bus_name = bus_name
    bus.bus_id = bus_id

    session.add(bus)
    session.commit()

    return f"{bus_name} created..."

@app.put("/buses")
def update_bus(buses: List[Bus]):

    for i in buses:
        bus = session.query(RouteTable).filter(RouteTable.bus_id == i.bus_id).first()
        bus.bus_id = i.bus_id
        bus.bus_name = i.bus_name
        session.commit()

    return f"{buses[0]} updated..."


@app.delete("/bus")
def delete_bus(bus_id: int):

    bus = session.query(RouteTable).filter(RouteTable.bus_id == bus_id).delete()
    session.commit()

    return f"{bus} deleted..."

read_buses()