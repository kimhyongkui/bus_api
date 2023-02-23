from api.route_data import get_route_data, get_all_route_data
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()


# 특정 경유노선의 전체정류소 DB 저장
def add_route_data(route_id):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        route_data_list = get_route_data(route_id)
        for route_data in route_data_list:
            sql = f"INSERT IGNORE INTO route_data (routeId, routeNm, stnOrd, stnNm, stnId)" \
                  f" VALUES ({route_data['routeId']}, " \
                  f"'{route_data['routeNm']}', " \
                  f"{route_data['stnOrd']}, " \
                  f"'{route_data['stnNm']}', " \
                  f"{route_data['stnId']})"
            curs.execute(sql)
        connection.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)


# 모든 노선의 정류소 DB저장
def add_all_route_data():
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        route_data_list = get_all_route_data()
        for route_data in route_data_list:
            sql = f"INSERT IGNORE INTO route_data (routeId, routeNm, stnOrd, stnNm, stnId)" \
                  f" VALUES ({route_data['routeId']}, " \
                  f"'{route_data['routeNm']}', " \
                  f"{route_data['stnOrd']}, " \
                  f"'{route_data['stnNm']}', " \
                  f"{route_data['stnId']})"
            curs.execute(sql)
            connection.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)
