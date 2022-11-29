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
#
def addBus() :
    for bus_data in bus_list:
        print(bus_data)
#
#         sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
#         curs.execute(sql)
#         conn.commit()
#
#     print("DB 저장 완료")
#     conn.close()

# def addStation() :
#     for station_data in station_list:
#         print(station_list)
    #     sql = f"INSERT INTO station (station_name, bus_id) VALUES ('{station_data['bus_name']}', {bus_data['bus_id']})"
    #     curs.execute(sql)
    #     conn.commit()
    #
    # print("DB 저장 완료")
    # conn.close()



