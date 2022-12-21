from api_bus import get_bus_all
from api_station import get_station_all, get_station
from api_vehicle import get_bus_info, get_bus_info_all
from api_arrive import get_arrive, get_arrive_all
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')


curs = conn.cursor()


# 노선데이터 -> 정류소데이터 or 차량데이터
# 차량데이터(vehid) -> 차량위치조회


# 각 노선의 아이디와 이름 DB저장
def add_bus_data():
    bus_list = get_bus_all()
    for bus_data in bus_list:
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
        curs.execute(sql)
        conn.commit()

    print("DB 저장 완료")
    conn.close()



#-----------------------------------------------------------------------

# 특정 노선의 정류소 DB저장
def add_station(busid):
    st_list = get_station(busid)
    for station_data in st_list:
        sql = f"INSERT INTO station (bus_id, station, stationNm, stationNo, gpsX, gpsY)" \
              f" VALUES ({station_data['bus_id']}, " \
              f"'{station_data['station']}', " \
              f"'{station_data['stationNm']}', " \
              f"'{station_data['stationNo']}', " \
              f"{station_data['gpsX']}, " \
              f"{station_data['gpsY']})"
        curs.execute(sql)
        conn.commit()
    print("정류소 저장 완료")
    conn.close()


# 모든 노선의 정류소 DB저장
def add_station_all():
    stall_list = get_station_all()
    for station_data in stall_list:
        sql = f"INSERT INTO station (bus_id, station, stationNm, stationNo, gpsX, gpsY)" \
              f" VALUES ({station_data['bus_id']}, " \
              f"'{station_data['station']}', " \
              f"'{station_data['stationNm']}', " \
              f"'{station_data['stationNo']}', " \
              f"{station_data['gpsX']}, " \
              f"{station_data['gpsY']})"
        curs.execute(sql)
        conn.commit()
    print("정류소 저장 완료")
    conn.close()

#-----------------------------------------------------------------------
# 특정 노선의 차량 DB저장
def add_veh_data(busid):
    veh_list = get_bus_info(busid)
    for vehicle_data in veh_list:
        sql = f"INSERT INTO vehicle (bus_id, vehId, plainNo)" \
              f"VALUES ({vehicle_data['bus_id']}, " \
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
        sql = f"INSERT IGNORE INTO vehicle (bus_id, vehId, plainNo)" \
              f"VALUES ({vehicle_data['bus_id']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        curs.execute(sql)
        conn.commit()
    print("차량 정보 저장 완료")
    conn.close()
#-----------------------------------------------------------------------
# 특정 경유노선의 전체정류소 DB 저장
def add_arrive(busid):
    arr_list = get_arrive(busid)
    for arr_data in arr_list:
        sql = f"INSERT INTO arrive (bus_id, rtNm, staOrd, stNm, stId)" \
              f" VALUES ({arr_data['bus_id']}, " \
              f"'{arr_data['rtNm']}', " \
              f"{arr_data['staOrd']}, " \
              f"'{arr_data['stNm']}', " \
              f"{arr_data['stId']})"

        curs.execute(sql)
        conn.commit()
    print("데이터 저장 완료")
    conn.close()



# 모든 노선의 정류소 DB저장
def add_arrive_all():
    arr_all_list = get_arrive_all()
    for arr_data in arr_all_list:
        sql = f"INSERT INTO arrive (bus_id, rtNm, staOrd, stNm, stId)" \
              f" VALUES ({arr_data['bus_id']}, " \
              f"'{arr_data['rtNm']}', " \
              f"{arr_data['staOrd']}, " \
              f"'{arr_data['stNm']}', " \
              f"{arr_data['stId']})"

        curs.execute(sql)
        conn.commit()
    print("데이터 저장 완료")
    conn.close()

