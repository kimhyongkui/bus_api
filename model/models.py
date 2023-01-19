from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db.db_connection import Base


class ArriveTable(Base):
    __tablename__ = 'arrive'
    routeId = Column(Integer, primary_key=True, nullable=False)
    routeNm = Column(String(45), nullable=False)
    stnOrd = Column(Integer, primary_key=True, nullable=False)
    stnNm = Column(String(45), nullable=False)
    stnId = Column(Integer, nullable=False)


class RouteTable(Base):
    __tablename__ = 'route'
    no = Column(Integer, primary_key=True, autoincrement=True)
    routeNm = Column(String(45), nullable=False)
    routeAbrv = Column(String(45), nullable=False)
    routeId = Column(Integer, nullable=False)


class StationTable(Base):
    __tablename__ = 'station'
    no = Column(Integer, primary_key=True, autoincrement=True)
    routeId = Column(Integer, nullable=False)
    routeNm = Column(String(45), nullable=False)
    routeAbrv = Column(String(45), nullable=False)
    stnId = Column(Integer, nullable=False)
    stnNm = Column(String(45), nullable=False)
    arsId = Column(String(45), nullable=False)
    direction = Column(String(45), nullable=False)
    gpsX = Column(Integer, nullable=False)
    gpsY = Column(Integer, nullable=False)


class VehicleTable(Base):
    __tablename__ = 'vehicle'
    routeId = Column(Integer, nullable=False)
    vehId = Column(Integer, primary_key=True, nullable=False)
    plainNo = Column(String(45), nullable=False)


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
