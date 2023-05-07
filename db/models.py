from sqlalchemy import VARCHAR, Column, Integer, Float, Boolean
from db.connection import Base


class Route_data(Base):
    __tablename__ = "route_data"

    routeId = Column(Integer, primary_key=True, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    stnOrd = Column(Integer, primary_key=True, nullable=False)
    stnNm = Column(VARCHAR(45), nullable=False)
    stnId = Column(Integer, nullable=False)


class Route_list(Base):
    __tablename__ = "route_list"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    routeAbrv = Column(VARCHAR(45), nullable=False)
    routeId = Column(Integer, nullable=False)


class Station(Base):
    __tablename__ = "station"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    routeId = Column(Integer, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    routeAbrv = Column(VARCHAR(45), nullable=False)
    stnId = Column(Integer, nullable=False)
    stnNm = Column(VARCHAR(45), nullable=False)
    arsId = Column(VARCHAR(45), nullable=True)
    direction = Column(VARCHAR(45), nullable=True)
    gpsX = Column(Float, nullable=False)
    gpsY = Column(Float, nullable=False)


class Vehicle(Base):
    __tablename__ = "vehicle"

    routeId = Column(Integer, nullable=False)
    vehId = Column(Integer, primary_key=True, nullable=False)
    plainNo = Column(VARCHAR(45), nullable=False)


class Account(Base):
    __tablename__ = "account"

    user_id = Column(VARCHAR(50), nullable=False, primary_key=True)
    pwd = Column(VARCHAR(100), nullable=False)
    permission = Column(Boolean, nullable=False)
