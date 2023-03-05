from api.route import get_all_route_list
from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import route_list
from dotenv import load_dotenv

Session = sessionmaker(bind=engine)
session = Session()

load_dotenv()


# 각 노선의 아이디와 이름 DB저장
def add_route_list():
    try:
        route_list_data = get_all_route_list()
        for data in route_list_data:
            result = route_list(
                routeNm=data['routeNm'],
                routeAbrv=data['routeAbrv'],
                routeId=data['routeId']
            )
            session.add(result)
        session.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        session.close()
