from api.vehicle import get_vehicle_data, get_all_vehicle_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Vehicle
from dotenv import load_dotenv
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 차량 DB저장
def add_veh_data(route_name):
    try:
        for data in get_vehicle_data(route_name):
            result = Vehicle(
                routeId=data['routeId'],
                vehId=data['vehId'],
                plainNo=data['plainNo']
            )
            session.add(result)
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


# 모든 노선의 차량 DB저장
def add_all_veh_data():
    try:
        for data in get_all_vehicle_data():
            result = Vehicle(
                routeId=data['routeId'],
                vehId=data['vehId'],
                plainNo=data['plainNo']
            )
            if not session.query(Vehicle).filter_by(vehId=data['vehId']).first():
                session.add(result)
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
