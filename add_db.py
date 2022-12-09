from api_bus import getBusAll
from api_station import getStationAll, getStation
from api_busvehid2 import getBusInfo, getBusInfoAll
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
def addbusdata():
    bus_list = getBusAll()
    for bus_data in bus_list:
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
        curs.execute(sql)
        conn.commit()

    print("DB 저장 완료")
    conn.close()

#-----------------------------------------------------------------------

# 특정 노선의 정류소 DB저장
def addstation():
    st_list = getStation()
    for station_data in st_list:
        sql = f"INSERT IGNORE INTO station (bus_id, station, stationNm, stationNo, gpsX, gpsY)" \
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
def addstationall():
    stall_list = getStationAll()
    for station_data in stall_list:
        sql = f"INSERT IGNORE INTO station (bus_id, station, stationNm, stationNo, gpsX, gpsY)" \
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
def addvehdata():
    veh_list = getBusInfo()
    for vehicle_data in veh_list:
        sql = f"INSERT IGNORE INTO vehicle (bus_id, vehId, plainNo)" \
              f"VALUES ({vehicle_data['bus_id']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        print(sql)
        curs.execute(sql)
        conn.commit()

    print("차량 정보 저장 완료")
    conn.close()

# 모든 노선의 차량 DB저장
def addvehalldata():
    vehall_list = getBusInfoAll()
    for vehicle_data in vehall_list:
        sql = f"INSERT IGNORE INTO vehicle (bus_id, vehId, plainNo)" \
              f"VALUES ({vehicle_data['bus_id']}, " \
              f"{vehicle_data['vehId']}, " \
              f"'{vehicle_data['plainNo']}')"
        curs.execute(sql)
        conn.commit()
    print("차량 정보 저장 완료")
    conn.close()

addvehalldata()
