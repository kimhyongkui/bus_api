from api.route_data import get_route_data, get_all_route_data
from db.get.db_data import get_all_route_list
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_data, test1
from dotenv import load_dotenv

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 특정 경유노선의 전체정류소 DB 저장
def add_route_data(route_id):
    try:
        route_data_data = get_route_data(route_id)
        for data in route_data_data:
            result = route_data(
                routeId=data['routeId'],
                routeNm=data['routeNm'],
                stnOrd=data['stnOrd'],
                stnNm=data['stnNm'],
                stnId=data['stnId']
            )
            session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()


# # 모든 노선의 정류소 DB저장
# def add_all_route_data():
#     try:
#         for data in get_all_route_data():
#             result = route_data(
#                 routeId=data['routeId'],
#                 routeNm=data['routeNm'],
#                 stnOrd=data['stnOrd'],
#                 stnNm=data['stnNm'],
#                 stnId=data['stnId']
#             )
#             session.add(result)
#             print(f"{data['routeId']}데이터 저장 완료")
#
#             try:
#                 session.commit()
#             except:
#                 print(f"{data['routeId']}데이터 저장 실패: 중복 데이터가 존재합니다.")
#
#         print('데이터 저장 완료')
#
#     except Exception as err:
#         return f"{err}"
#
#     finally:
#         session.close()

def add_all_route_data():
    try:
        for route_id in get_all_route_list():
            result = get_route_data(route_id['routeId'])
            for data in result:
                result = test1(
                    routeId=data['routeId'],
                    routeNm=data['routeNm'],
                    stnOrd=data['stnOrd'],
                    stnNm=data['stnNm'],
                    stnId=data['stnId']
                )
            try:
                session.add(result)
                print(f"{route_id['routeId']}데이터 저장 완료")
            except:
                print(f"{route_id['routeId']}데이터 저장 실패: 중복 데이터가 존재합니다.")

        session.commit()
        print('데이터 저장 완료')

    except Exception as err:

        return f"{err}"

    finally:
        session.close()

add_all_route_data()
