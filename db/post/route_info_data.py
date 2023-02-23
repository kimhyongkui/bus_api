from api.route_data import get_route_data, get_all_route_data
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()


# 특정 경유노선의 전체정류소 DB 저장
def add_route_info(route_id):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        arr_list = get_route_data(route_id)
        for arr_data in arr_list:
            sql = f"INSERT IGNORE INTO route_data (routeId, routeNm, stnOrd, stnNm, stnId)" \
                  f" VALUES ({arr_data['routeId']}, " \
                  f"'{arr_data['routeNm']}', " \
                  f"{arr_data['stnOrd']}, " \
                  f"'{arr_data['stnNm']}', " \
                  f"{arr_data['stnId']})"
            curs.execute(sql)
        connection.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)


# 모든 노선의 정류소 DB저장
def add_route_info_all():
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        arr_all_list = get_all_route_data()
        for arr_data in arr_all_list:
            sql = f"INSERT IGNORE INTO route_data (routeId, routeNm, stnOrd, stnNm, stnId)" \
                  f" VALUES ({arr_data['routeId']}, " \
                  f"'{arr_data['routeNm']}', " \
                  f"{arr_data['stnOrd']}, " \
                  f"'{arr_data['stnNm']}', " \
                  f"{arr_data['stnId']})"
            curs.execute(sql)
            connection.commit()
        print('데이터 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)
