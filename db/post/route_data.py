from api.route_data import get_route_data, get_all_route_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Route_data
from dotenv import load_dotenv
from fastapi import status, HTTPException

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 경유노선의 전체정류소 DB 저장
def add_route_data(route_id):
    try:
        route_data_data = get_route_data(route_id)
        for data in route_data_data:
            result = Route_data(
                routeId=data['routeId'],
                routeNm=data['routeNm'],
                stnOrd=data['stnOrd'],
                stnNm=data['stnNm'],
                stnId=data['stnId']
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


# 모든 노선의 정류소 DB저장
def add_all_route_data():
    try:
        route_all_list = get_all_route_data()
        for data in route_all_list:
            result = Route_data(
                routeId=data['routeId'],
                routeNm=data['routeNm'],
                stnOrd=data['stnOrd'],
                stnNm=data['stnNm'],
                stnId=data['stnId']
            )
            if not session.query(Route_data).\
                    filter(Route_data.routeId == data['routeId'], Route_data.stnOrd == data['stnOrd']).\
                    first():
                session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
