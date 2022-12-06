from api_bus import getBusAll
# from api_station import getStationAll
from api_station2 import geturl
from api_busvehid import getBusInfo
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')


curs = conn.cursor()

bus_list = getBusAll()
# station_list = getStationAll()
station_list = geturl()
vehicle_list = getBusInfo()



# 노선데이터 -> 정류소데이터 or 차량데이터
# 차량데이터(vehid) -> 차량위치조회



def addbusdata():
    for bus_data in bus_list:
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
        curs.execute(sql)
        conn.commit()

    print("DB 저장 완료")
    conn.close()



def addstationdata():
    for station_data in station_list:
        sql = f"INSERT IGNORE INTO station (station, stationNm, stationNo, gpsX, gpsY)" \
              f" VALUES ({station_data['station']}, " \
              f"'{station_data['stationNm']}', " \
              f"'{station_data['stationNo']}', " \
              f"{station_data['gpsX']}, " \
              f"{station_data['gpsY']})"
        curs.execute(sql)
        conn.commit()
    print("정류소 저장 완료")
    conn.close()

addstationdata()
#
# def addvehicledata():
#     for id in bus_list:
#         bus_id = id['bus_id']
#         for vehicle_data in vehicle_list:
#             sql = f"INSERT IGNORE INTO vehicle (bus_id, vehId, plainNo)" \
#                   f"VALUES ({bus_id}, " \
#                   f"{vehicle_data['vehId']}, " \
#                   f"'{vehicle_data['plainNo']}')"
#             print(sql)
#             curs.execute(sql)
#             conn.commit()
#
#     print("차량 정보 저장 완료")
#     conn.close()
#
# addvehicledata()

# def addvehicledata():
#     for vehicle_data in vehicle_list:
#         sql = f"INSERT IGNORE INTO vehicle (bus_id, vehId, plainNo)" \
#               f"VALUES ({bus_id}, " \
#               f"{vehicle_data['vehId']}, " \
#               f"'{vehicle_data['plainNo']}')"
#         curs.execute(sql)
#         conn.commit()
#     print("차량 정보 저장 완료")
#     conn.close()
#
# addvehicledata()

