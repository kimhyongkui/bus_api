from dotenv import load_dotenv
from api_bus import get_busall
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')

bus_list = get_busall()


# get(n번째)
def get_data(table, n):
    curs = conn.cursor()
    sql = f"SELECT * FROM {table}"
    curs.execute(sql)
    data = curs.fetchall()
    print(data[n-1])
    conn.close()

#-----------------------------------------------------------------------------

# get(특정)
def get_some_data(table, column, value):
    curs = conn.cursor()
    sql = f"SELECT * FROM {table} WHERE {column}={value}"
    curs.execute(sql)
    result = curs.fetchall()
    for i in result:
        print(i)
    conn.close()

#-----------------------------------------------------------------------------

# get(전체)
def get_all_data(table):
    curs = conn.cursor()
    sql = f"SELECT * FROM {table}"
    curs.execute(sql)
    result = curs.fetchall()
    conn.commit()
    for i in result:
        print(i)
    conn.close()


#-----------------------------------------------------------------------------

# 두 개의 테이블을 묶어서 조회하는 방법
# select A테이블.컬럼a,컬럼b, B테이블.컬럼c,컬럼d from A테이블 join B테이블 using(컬럼명);
def get_mix_data():
    curs = conn.cursor()
    sql = f"SELECT {input('테이블A.컬럼명, 테이블B.컬럼명 : ')} from {input('테이블 : ')} join {input('테이블 : ')} using ({input('컬럼명 : ')})"
    curs.execute(sql)
    result = curs.fetchall()
    for station in result:
        print(station)
    conn.close()

#-----------------------------------------------------------------------------

# 정류소 테이블에서 특정 역을 검색해서 노선id, 역id, 역이름 조회하기

#-----------------------------------------------------------------------------

# 정류소를 검색시 해당 정류소를 지나는 노선의 이름과 id를 출력하기
def get_station_bus():
    curs = conn.cursor()
    sql = f"SELECT bus.bus_id, bus_name, station.stationNm " \
          f"from bus join station using (bus_id) where stationNm = '{input('역이름: ')}'"
    curs.execute(sql)
    result = curs.fetchall()
    for station in result:
        print(station)
    conn.close()



#-----------------------------------------------------------------------------

# post(전체)

def post_all():
    curs = conn.cursor()
    for bus_data in bus_list:
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
        curs.execute(sql)
        conn.commit()
    conn.close()
#
#-----------------------------------------------------------------------------
# post(일부)
def post_some_data():
    curs = conn.cursor()
    sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ({input('name : ')}, {input('id : ')})"
    curs.execute(sql)
    conn.commit()
    conn.close()
#
#-----------------------------------------------------------------------------

# put
def put_data():
    curs = conn.cursor()
    sql = f"UPDATE bus SET bus_name={input('name : ')} WHERE bus_name={input('id : ')}"
    curs.execute(sql)
    conn.commit()
    conn.close()

#-----------------------------------------------------------------------------

# delete
def delete_data():
    curs = conn.cursor()
    sql = f"DELETE FROM bus WHERE bus_name={input('버스이름 : ')}"
    curs.execute(sql)
    conn.commit()

    conn.close()


#-----------------------------------------------------------------------------

# DB 초기화 with auto_increment 초기화
def reset_table(table):
    curs = conn.cursor()
    sql = f"DELETE FROM {table}"
    curs.execute(sql)
    conn.commit()

    curs.execute(sql)
    sql = f"ALTER TABLE {table} AUTO_INCREMENT = 1"

    conn.close()

#-----------------------------------------------------------------------------
