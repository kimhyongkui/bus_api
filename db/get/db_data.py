from db.connection import conn


def get_stn_data(stn_nm, stn_id):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        sql = f"SELECT * FROM route_data WHERE stnNm = '{stn_nm}' AND stnId = {stn_id}"
        curs.execute(sql)
        result = curs.fetchall()

        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'

    except Exception as err:
        result = f"{err}, 정류소 이름 또는 ID를 확인하세요"

    finally:
        conn.release(connection)

    return result


def get_route_list(route_nm):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        sql = f"SELECT routeNm, stnOrd, stnNm FROM route_data WHERE routeNm Like '%{route_nm}%'"
        curs.execute(sql)
        result = curs.fetchall()

        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        conn.release(connection)

    return result


def get_route_data(route_nm):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        sql = f"SELECT * FROM route WHERE routeNm Like '%{route_nm}%'"
        curs.execute(sql)
        result = curs.fetchone()

        if not result:
            result = '데이터가 없습니다. 다시 검색하세요'

    except Exception as err:
        result = f"{err}, 노선 이름을 확인하세요"

    finally:
        conn.release(connection)

    return result


def get_stn_name(stn_nm):
    conn.init()
    connection = conn.get_conn()
    curs = connection.cursor()
    try:
        sql = f"SELECT stnNm, stnId, arsId, direction FROM station WHERE stnNm Like '%{stn_nm}%' GROUP BY stnId"
        curs.execute(sql)
        result = curs.fetchall()

        if not result:
            result = '다시 검색하세요'

    except Exception as err:
        result = f"{err}, 다시 검색하세요"

    finally:
        conn.release(connection)

    return result
