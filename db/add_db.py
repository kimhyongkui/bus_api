from api.api_route import get_route_all
from api.api_station import get_station_all, get_station
from api.api_vehicle import get_bus_info, get_bus_info_all
from api.api_route_info import get_route_info, get_route_info_all
from dotenv import load_dotenv
from db_connection import conn

load_dotenv()

curs = conn.cursor()


# 노선데이터 -> 정류소데이터 or 차량데이터
# 차량데이터(vehid) -> 차량위치조회


# 각 노선의 아이디와 이름 DB저장
def add_route_data():
    route_list = get_route_all()
    for route_data in route_list:
        sql = f"INSERT INTO route (routeNm, routeAbrv, routeId) " \
              f"VALUES ('{route_data['routeNm']}', '{route_data['routeAbrv']}', {route_data['routeId']})"
        curs.execute(sql)
        conn.commit()

    print("DB 저장 완료")
    conn.close()


# -----------------------------------------------------------------------

# 특정 노선의 정류소 DB저장
def add_station(routeid):
    stn_list = get_station(routeid)
    for stn_data in stn_list:
        sql = f"INSERT INTO station (routeId, routeNm, routeAbrv, stnId, stnNm, arsId, direction, gpsX, gpsY)" \
              f" VALUES ({stn_data['routeId']}, " \
              f"'{stn_data['routeNm']}', " \
              f"'{stn_data['routeAbrv']}', " \
              f"{stn_data['stnId']}, " \
              f"'{stn_data['stnNm']}', " \
              f"'{stn_data['arsId']}', " \
              f"'{stn_data['direction']}', " \
              f"{stn_data['gpsX']}, " \
              f"{stn_data['gpsY']})"
        curs.execute(sql)
        conn.commit()
    print("정류소 저장 완료")
    conn.close()


# 모든 노선의 정류소 DB저장
def add_station_all():
    stn_all_list = get_station_all()
    for stn_data in stn_all_list:
        sql = f"INSERT INTO station (routeId, routeNm, routeAbrv, stnId, stnNm, arsId, direction, gpsX, gpsY)" \
              f" VALUES ({stn_data['routeId']}, " \
              f"'{stn_data['routeNm']}', " \
              f"'{stn_data['routeAbrv']}', " \
              f"{stn_data['stnId']}, " \
              f"'{stn_data['stnNm']}', " \
              f"'{stn_data['arsId']}', " \
              f"'{stn_data['direction']}', " \
              f"{stn_data['gpsX']}, " \
              f"{stn_data['gpsY']})"
        curs.execute(sql)
        conn.commit()
    print("정류소 저장 완료")
    conn.close()


# -----------------------------------------------------------------------
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


# -----------------------------------------------------------------------
# 특정 경유노선의 전체정류소 DB 저장
def add_arrive(routeid):
    arr_list = get_route_info(routeid)
    for arr_data in arr_list:
        sql = f"INSERT IGNORE INTO arrive (routeId, routeNm, stnOrd, stnNm, stnId)" \
              f" VALUES ({arr_data['routeId']}, " \
              f"'{arr_data['routeNm']}', " \
              f"{arr_data['stnOrd']}, " \
              f"'{arr_data['stnNm']}', " \
              f"{arr_data['stnId']})"

        curs.execute(sql)
        conn.commit()
    print("데이터 저장 완료")
    conn.close()


# 모든 노선의 정류소 DB저장
def add_arrive_all():
    arr_all_list = get_route_info_all()
    for arr_data in arr_all_list:
        sql = f"INSERT IGNORE INTO arrive (routeId, routeNm, stnOrd, stnNm, stnId)" \
              f" VALUES ({arr_data['routeId']}, " \
              f"'{arr_data['routeNm']}', " \
              f"{arr_data['stnOrd']}, " \
              f"'{arr_data['stnNm']}', " \
              f"{arr_data['stnId']})"

        curs.execute(sql)
        conn.commit()
    print("데이터 저장 완료")
    conn.close()
