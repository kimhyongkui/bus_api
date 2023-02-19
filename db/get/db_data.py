from db.connection import conn


def get_stn_data(stnNm, stnId):
    try:
        conn.init()
        connection = conn.get_conn()
        curs = connection.cursor()
        sql = f"SELECT * FROM route_info WHERE stnNm='{stnNm}' AND stnId={stnId}"
        curs.execute(sql)
        result = curs.fetchall()
        conn.release(connection)
        if not result:
            result = '다시 검색하세요'
    except Exception as err:
        result = f"{err}, 다시 검색하세요"
    return result


def get_route_list(routeNm):
    try:
        conn.init()
        connection = conn.get_conn()
        curs = connection.cursor()
        sql = f"SELECT routeNm, stnOrd, stnNm FROM route_info WHERE routeNm = '{routeNm}'"
        curs.execute(sql)
        result = curs.fetchall()
        conn.release(connection)
        if not result:
            result = '다시 검색하세요'
    except Exception as err:
        result = f"{err}, 다시 검색하세요"
    return result


def get_route_name(routeNm):
    try:
        conn.init()
        connection = conn.get_conn()
        curs = connection.cursor()
        sql = f"SELECT * FROM route WHERE routeNm = '{routeNm}'"
        curs.execute(sql)
        result = curs.fetchone()
        conn.release(connection)
        if result:
            result = result[3]
        else:
            result = '다시 검색하세요'
    except Exception as err:
        result = f"{err}, 다시 검색하세요"
    return result


def get_stn_name(stnNm):
    try:
        conn.init()
        connection = conn.get_conn()
        curs = connection.cursor()
        sql = f"SELECT stnNm, stnId, arsId, direction FROM station WHERE stnNm = '{stnNm}' GROUP BY stnId"
        curs.execute(sql)
        result = curs.fetchall()
        conn.release(connection)
        if not result:
            result = '다시 검색하세요'
    except Exception as err:
        result = f"{err}, 다시 검색하세요"
    return result
