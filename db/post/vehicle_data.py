from api.vehicle import get_bus_info, get_bus_info_all
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()

curs = conn.cursor()


# 특정 노선의 차량 DB저장
def add_veh_data(routeid):
    vehicle_list = get_bus_info(routeid)
    for vehicle_data in vehicle_list:
        sql = f"INSERT INTO vehicle (routeId, vehId, plainNo)" \
              f"VALUES ({vehicle_data['routeId']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        curs.execute(sql)
        conn.commit()

    print("차량 정보 저장 완료")
    conn.close()


# 모든 노선의 차량 DB저장
def add_veh_all_data():
    veh_all_list = get_bus_info_all()
    for vehicle_data in veh_all_list:
        sql = f"INSERT IGNORE INTO vehicle (routeId, vehId, plainNo)" \
              f"VALUES ({vehicle_data['routeId']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        curs.execute(sql)
        conn.commit()
    print("차량 정보 저장 완료")
    conn.close()
