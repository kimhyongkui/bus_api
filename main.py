from fastapi import FastAPI
from typing import List
from db import session
from models import BusTable, Bus

app = FastAPI()


@app.get("/buses")
def read_buses():
    buses = session.query(BusTable).all()
    return buses

@app.get("/buses/{bus_id}")
def read_bus(bus_id: int):
    bus = session.query(BusTable).filter(BusTable.bus_id == bus_id).first()
    return bus

@app.post("/bus")
def create_bus(bus_name: str, bus_id: int):

    bus = BusTable()
    bus.bus_name = bus_name
    bus.bus_id = bus_id

    session.add(bus)
    session.commit()

    return f"{bus_name} created..."

@app.put("/buses")
def update_bus(buses: List[Bus]):

    for i in buses:
        bus = session.query(BusTable).filter(BusTable.bus_id == i.bus_id).first()
        bus.bus_id = i.bus_id
        bus.bus_name = i.bus_name
        session.commit()

    return f"{buses[0]} updated..."


@app.delete("/bus")
def delete_bus(bus_id: int):

    bus = session.query(BusTable).filter(BusTable.bus_id == bus_id).delete()
    session.commit()

    return f"{bus} deleted..."

