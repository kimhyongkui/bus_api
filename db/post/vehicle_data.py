from api.vehicle import get_vehicle_data, get_all_vehicle_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import vehicle
from dotenv import load_dotenv
from fastapi import status, HTTPException

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 차량 DB저장
def add_veh_data(route_name):
    try:
        for data in get_vehicle_data(route_name):
            result = vehicle(
                routeId=data['routeId'],
                vehId=data['vehId'],
                plainNo=data['plainNo']
            )
            session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


# 모든 노선의 차량 DB저장
def add_veh_all_data():
    try:
        for data in get_all_vehicle_data():
            result = vehicle(
                routeId=data['routeId'],
                vehId=data['vehId'],
                plainNo=data['plainNo']
            )
            if not session.query(vehicle).filter_by(vehId=data['vehId']).first():
                session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
