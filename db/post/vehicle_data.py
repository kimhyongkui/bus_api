from api.vehicle import get_vehicle_data, get_all_vehicle_data
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()


# 특정 노선의 차량 DB저장
def add_veh_data(route_name):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        vehicle_list = get_vehicle_data(route_name)
        for vehicle_data in vehicle_list:
            sql = f"INSERT INTO vehicle (routeId, vehId, plainNo)" \
                  f"VALUES ({vehicle_data['routeId']}, " \
                  f"{vehicle_data['vehId']}, " \
                  f"'{vehicle_data['plainNo']}')"
            curs.execute(sql)
        connection.commit()
        print('DB 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)


# 모든 노선의 차량 DB저장
def add_veh_all_data():
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        veh_all_list = get_all_vehicle_data()
        for vehicle_data in veh_all_list:
            sql = f"INSERT IGNORE INTO vehicle (routeId, vehId, plainNo)" \
                  f"VALUES ({vehicle_data['routeId']}, " \
                  f"{vehicle_data['vehId']}, " \
                  f"'{vehicle_data['plainNo']}')"
            curs.execute(sql)
        connection.commit()
        print('DB 저장 완료')

    except Exception as err:
        return f"{err}"

    finally:
        conn.release(connection)
