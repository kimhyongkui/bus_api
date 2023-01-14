from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base


class RouteTable(Base):
    __tablename__ = 'Route'
    no = Column(Integer, primary_key=True, autoincrement=True)
    routeNm = Column(String(45), nullable=False)
    routeAbrv = Column(String(45), nullable=False)
    routeId = Column(Integer, nullable=False)


class Arrive(BaseModel):
    routeId: int
    routeNm: str
    stnOrd: int
    stnNm: str
    stnId: int


class Route(BaseModel):
    no: int
    routeNm: str
    routeAbrv: str
    routeId: int


class Station(BaseModel):
    no: int
    routeId: int
    routeNm: str
    routeAbrv: str
    stnId: int
    stnNm: str
    arsId: str
    direction: str
    gpsX: int
    gpsY: int

class Vehicle(BaseModel):
    routeid: int
    vehId: int
    plainNo: str

