from api_bus import get_busall
from api_station import get_stationall, get_station
from api_busvehid import get_businfo, get_businfoall
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
def add_busdata():
    bus_list = get_busall()
    for bus_data in bus_list:
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
        curs.execute(sql)
        conn.commit()

    print("DB 저장 완료")
    conn.close()



#-----------------------------------------------------------------------

# 특정 노선의 정류소 DB저장
def add_station():
    st_list = get_station()
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
def add_stationall():
    stall_list = get_stationall()
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
def add_vehdata():
    veh_list = get_businfo()
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
def add_vehalldata():
    vehall_list = get_businfoall()
    for vehicle_data in vehall_list:
        sql = f"INSERT INTO vehicle (bus_id, vehId, plainNo)" \
              f"VALUES ({vehicle_data['bus_id']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        curs.execute(sql)
        conn.commit()
    print("차량 정보 저장 완료")
    conn.close()

