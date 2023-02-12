from api.station import get_station_all, get_station
from dotenv import load_dotenv
from db.connection import conn

load_dotenv()

curs = conn.cursor()


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
