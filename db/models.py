from sqlalchemy import VARCHAR, Column, Integer, Float
from db.connection import Base


class route_data(Base):
    __tablename__ = "route_data"

    routeId = Column(Integer, primary_key=True, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    stnOrd = Column(Integer, primary_key=True, nullable=False)
    stnNm = Column(VARCHAR(45), nullable=False)
    stnId = Column(Integer, nullable=False)


class route_list(Base):
    __tablename__ = "route_list"

    no = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    routeAbrv = Column(VARCHAR(45), nullable=False)
    routeId = Column(Integer, nullable=False)


class station(Base):
    __tablename__ = "station"

    no = Column(Integer, primary_key=True, nullable=False)
    routeId = Column(Integer, nullable=False)
    routeNm = Column(VARCHAR(45), nullable=False)
    routeAbrv = Column(VARCHAR(45), nullable=False)
    stnId = Column(Integer, nullable=False)
    stnNm = Column(VARCHAR(45), nullable=False)
    arsId = Column(VARCHAR(45), nullable=False)
    direction = Column(VARCHAR(45), nullable=False)
    gpsX = Column(Float, nullable=False)
    gpsY = Column(Float, nullable=False)


class vehicle(Base):
    __tablename__ = "vehicle"

    routeId = Column(Integer, nullable=False)
    vehId = Column(Integer, primary_key=True, )
    plainNo = Column(VARCHAR(45), nullable=False)
