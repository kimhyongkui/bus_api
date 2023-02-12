from db.connection import conn


def get_stn_data(stnNm, stnId):
    curs = conn.cursor()
    sql = f"SELECT * FROM route_info WHERE stnNm='{stnNm}' AND stnId={stnId}"
    curs.execute(sql)
    result = curs.fetchall()
    return result


def get_route_list(routeNm):
    curs = conn.cursor()
    sql = f"SELECT routeNm, stnOrd, stnNm FROM route_info WHERE routeNm = '{routeNm}'"
    curs.execute(sql)
    result = curs.fetchall()
    return result


def get_route_name(routeNm):
    curs = conn.cursor()
    sql = f"SELECT * FROM route WHERE routeNm = '{routeNm}'"
    curs.execute(sql)
    result = curs.fetchone()
    return result[3]


def get_stn_name(stnNm):
    curs = conn.cursor()
    sql = f"SELECT stnNm, stnId, arsId, direction FROM station WHERE stnNm = '{stnNm}' GROUP BY stnId"
    curs.execute(sql)
    result = curs.fetchall()
    return result
