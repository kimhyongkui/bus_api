from api.station import get_station_data, get_all_station_data
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Station
from dotenv import load_dotenv
from fastapi import status, HTTPException
from fastapi.responses import JSONResponse
from db.get.db_data import get_route_list

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 정류소 DB저장
def add_station_data(route_id):
    try:
        for data in get_station_data(route_id):
            result = Station(
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
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()


# # 모든 노선의 정류소 DB저장
# def add_all_station_data():
#     try:
#         for data in get_all_station_data():
#             result = Station(
#                 routeId=data['routeId'],
#                 routeNm=data['routeNm'],
#                 routeAbrv=data['routeAbrv'],
#                 stnId=data['stnId'],
#                 stnNm=data['stnNm'],
#                 arsId=data['arsId'],
#                 direction=data['direction'],
#                 gpsX=data['gpsX'],
#                 gpsY=data['gpsY']
#             )
#             session.add(result)
#         session.commit()
#         return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})
#
#     except HTTPException:
#         raise
#
#     except Exception as err:
#         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))
#
#     finally:
#         session.close()

def add_all_station_data2():
    try:
        for route_id in get_route_list():
            stn_data = get_station_data(route_id['routeId'])
            for data in stn_data:
                result = Station(
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
                if not session.query(Station).filter_by(
                        routeId=data['routeId'],
                        routeNm=data['routeNm'],
                        routeAbrv=data['routeAbrv'],
                        stnId=data['stnId'],
                        stnNm=data['stnNm'],
                        arsId=data['arsId'],
                        direction=data['direction'],
                        gpsX=data['gpsX'],
                        gpsY=data['gpsY']
                ).first():
                    session.add(result)
        session.commit()
        return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "데이터 저장 완료"})

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(err))

    finally:
        session.close()
