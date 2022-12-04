from api_bus import getBusAll
from api_station import getStationAll
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')


curs = conn.cursor()

bus_list = getBusAll()
station_list = getStationAll()




# def addbusdata():
#     for bus_data in bus_list:
#         sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
#         curs.execute(sql)
#         conn.commit()
#
#     print("DB 저장 완료")
#     conn.close()



def addstationdata():
    for station_data in station_list:
        sql = f"INSERT INTO station (station, stationNm, stationNo, gpsX, gpsY)" \
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



