from db.db_connection import conn

def get_stn_data(stnNm, stnId):
    curs = conn.cursor()
    sql = f"SELECT * FROM route_info WHERE stnNm='{stnNm}' AND stnId={stnId}"
    curs.execute(sql)
    result = curs.fetchall()

    return result

def get_routeNm(routeNm):
    curs = conn.cursor()
    sql = f"SELECT * FROM route WHERE routeNm='{routeNm}'"
    curs.execute(sql)
    result = curs.fetchone()

    return result[3]


