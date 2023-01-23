from fastapi import APIRouter

router = APIRouter()

# @router.put("/buses")
# def update_bus(buses: List[Bus]):
#
#     for i in buses:
#         bus = session.query(BusTable).filter(BusTable.bus_id == i.bus_id).first()
#         bus.bus_id = i.bus_id
#         bus.bus_name = i.bus_name
#         session.commit()
#
#     return f"{buses[0]} updated..."
#

