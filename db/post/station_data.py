from api.station import get_station_data, get_all_station_data
from db.get.db_data import get_route_list
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from db.connection import engine
from db.models import station, test3, test1
from dotenv import load_dotenv

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 노선의 정류소 DB저장
def add_station(route_id):
    try:
        stn_data = get_station_data(route_id)
        if stn_data:
            for data in stn_data:
                result = test3(
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
            print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()
# add_station(229000030)

# 모든 노선의 정류소 DB저장
def add_station_all():
    stn_all_list = get_all_station_data()
    # records = []
    for data in stn_all_list:
        record = test1(
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
        # records.append(record)
    # session.add_all(records)
        session.add()
    session.commit()
    print('데이터 저장 완료')



# # 모든 노선의 정류소 DB저장
# def add_station_all():
#     try:
#         for route_id in get_route_list():
#             result = get_station_data(route_id['routeId'])
#             records = []
#             for data in result:
#                 record = test3(
#                     routeId=data['routeId'],
#                     routeNm=data['routeNm'],
#                     routeAbrv=data['routeAbrv'],
#                     stnId=data['stnId'],
#                     stnNm=data['stnNm'],
#                     arsId=data['arsId'],
#                     direction=data['direction'],
#                     gpsX=data['gpsX'],
#                     gpsY=data['gpsY']
#                 )
#                 records.append(record)
#             try:
#                 session.add_all(records)
#                 session.commit()
#                 print(f"{route_id['routeId']} 데이터 저장 완료")
#             except TypeError:
#                 session.rollback()
#                 print(f"{route_id['routeId']} 데이터 저장 실패: 데이터가 없습니다.")
#             except IntegrityError:
#                 session.rollback()
#                 print(f"{route_id['routeId']} 데이터 저장 실패: 중복 데이터가 존재합니다.")
#
#         print('진짜 저장 끝')
#
#     except Exception as err:
#         session.rollback()
#         return f"{err}"
#
#     finally:
#         session.close()

