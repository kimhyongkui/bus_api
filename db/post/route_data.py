from api.route import get_route_all
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()


# 각 노선의 아이디와 이름 DB저장
def add_route_data():
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        route_list = get_route_all()
        for route_data in route_list:
            sql = f"INSERT INTO route (routeNm, routeAbrv, routeId) " \
                  f"VALUES ('{route_data['routeNm']}', '{route_data['routeAbrv']}', {route_data['routeId']})"
            curs.execute(sql)
        connection.commit()
        print('DB 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)

