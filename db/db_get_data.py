from db_connection import conn

def get_data(stnNm, stnId):
    curs = conn.cursor()
    sql = f"SELECT * FROM arrive WHERE stnNm='{stnNm}' AND stnId={stnId}"
    curs.execute(sql)
    result = curs.fetchall()

    return result

