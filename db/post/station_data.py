from api.station import get_station_data, get_all_station_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import station, test1
from dotenv import load_dotenv
from fastapi import status
from fastapi.responses import JSONResponse

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 정류소 DB저장
def add_station(route_id):
    try:
        stn_data = get_station_data(route_id)
        if stn_data:
            for data in stn_data:
                result = test1(
                    routeId=data['routeId'],
                    routeNm=data['routeNm'],
                    routeAbrv=data['routeAbrv'],
                    stnId=data['stnId'],
                    stnNm=data['stnNm'],
                    arsId=data['arsId'],
                    direction=data['direction'],
                    gpsX=data['gpsX'],
                    gpsY=data['gpsY']
                )
                session.add(result)
            session.commit()
            return JSONResponse(
                status_code=status.HTTP_201_CREATED,
                content={"message": "데이터가 저장됨"}
            )
        else:
            return JSONResponse(
                status_code=status.HTTP_204_NO_CONTENT,
                content={"message": "데이터가 없음"}
            )

    except Exception as err:
        raise Exception(str(err))

    finally:
        session.close()


# 모든 노선의 정류소 DB저장
def add_station_all():
    try:
        stn_all_list = get_all_station_data()
        for data in stn_all_list:
            record = station(
                routeId=data['routeId'],
                routeNm=data['routeNm'],
                routeAbrv=data['routeAbrv'],
                stnId=data['stnId'],
                stnNm=data['stnNm'],
                arsId=data['arsId'],
                direction=data['direction'],
                gpsX=data['gpsX'],
                gpsY=data['gpsY']
            )
            session.add(record)
        session.commit()
        print('데이터 저장 완료')
    except Exception as err:
        raise Exception(str(err))
    finally:
        session.close()


