from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from connection import Base


class route_data(Base):
    __tablename__ = "route_data"

    routeId = Column(Integer, primary_key=True)
    routeNm = Column(String, unique=True, index=True)
    stnOrd = Column(Integer, primary_key=True)
    stnNm = Column(String)
    stnId = Column(Integer)

    items = relationship("Item", back_populates="owner")


class route_list(Base):
    __tablename__ = "route_list"

    no = Column(Integer, primary_key=True, AutoIncrement=True)
    routeNm = Column(String)
    routeAbrv = Column(String)
    routeId = Column(Integer)

    owner = relationship("User", back_populates="items")


class station(Base):
    __tablename__ = "station"

    no = Column(Integer, primary_key=True, index=True)
    routeId = Column(Integer)
    routeNm = Column(String)
    routeAbrv = Column(String)
    stnId = Column(Integer)
    stnNm = Column(String)
    ArsId = Column(String)
    direction = Column(String)
    gpsX = Column(String)
    gpsY = Column(String)

    owner = relationship("User", back_populates="items")


class vehicle(Base):
    __tablename__ = "vehicle"

    routeId = Column(Integer)
    vehId = Column(Integer, primary_key=True,)
    plainNo = Column(String)

    owner = relationship("User", back_populates="items")
