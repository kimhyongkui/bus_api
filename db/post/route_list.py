from api.route import get_all_route_list
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import test_table
from dotenv import load_dotenv

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 각 노선의 아이디와 이름 DB저장
def add_route_list():

    try:
        all_route_list = get_all_route_list()

        for route_data in all_route_list:
            route = test_table(
                no=route_data['no'],
                routeNm=route_data['routeNm'],
                routeAbrv=route_data['routeAbrv'],
                routeId=route_data['routeId']
            )
            session.add(route)
        session.commit()
        print('DB 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()

print(add_route_list())