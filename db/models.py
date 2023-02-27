from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from connection import Base


class route_data(Base):
    __tablename__ = "route_data"

    routeId = Column(Integer, primary_key=True, index=True)
    routeNm = Column(String, unique=True, index=True)
    stnOrd = Column(String)
    stnNm = Column(Boolean, default=True)
    stnId = Column(Boolean, default=True)
    items = relationship("Item", back_populates="owner")


class route_list(Base):
    __tablename__ = "route_list"

    no = Column(Integer, primary_key=True, index=True)
    routeNm = Column(String, index=True)
    routeAbrv = Column(String, index=True)
    routeId = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class station(Base):
    __tablename__ = "station"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class vehicle(Base):
    __tablename__ = "vehicle"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
