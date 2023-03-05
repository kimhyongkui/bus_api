from api.vehicle import get_vehicle_data, get_all_vehicle_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import vehicle, test2
from dotenv import load_dotenv

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 차량 DB저장
def add_veh_data(route_name):
    try:
        vehicle_list_data = get_vehicle_data(route_name)
        for data in vehicle_list_data:
            if data:
                result = vehicle(
                    routeId=data['routeId'],
                    vehId=data['vehId'],
                    plainNo=data['plainNo']
                )
                session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()


# 모든 노선의 차량 DB저장
def add_veh_all_data():
    try:
        veh_all_list_data = get_all_vehicle_data()
        for data in veh_all_list_data:
            if data:
                result = vehicle(
                    routeId=data['routeId'],
                    vehId=data['vehId'],
                    plainNo=data['plainNo']
                )
                session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()
