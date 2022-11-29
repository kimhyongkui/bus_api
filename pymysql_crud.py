from dotenv import load_dotenv
from bus_api import getBusAll
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')

bus_list = getBusAll()


# get(n번째)

# curs = conn.cursor()
# sql = "SELECT * FROM bus"
# curs.execute(sql)

# data = curs.fetchall()
# print(data[int(input('n번째 : '))-1])

# conn.close()

#-----------------------------------------------------------------------------

# get(특정)

# curs = conn.cursor()
# sql = f"SELECT * FROM bus WHERE bus_name={input('버스번호 : ')}"
# curs.execute(sql)

# result = curs.fetchall()
# for bus in result:
#     print(bus)

# conn.close()

#-----------------------------------------------------------------------------

# get(전체)

# curs = conn.cursor()
# sql = "SELECT * FROM bus"
# curs.execute(sql)
# result = curs.fetchall()
# conn.commit()
# for i in result:
#     print(i)
#
# conn.close()
#-----------------------------------------------------------------------------
# post(전체)

# curs = conn.cursor()

# for bus_data in bus_list:
#     sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
#     curs.execute(sql)
#     conn.commit()
#
# conn.close()
#
#-----------------------------------------------------------------------------
# post(일부)

curs = conn.cursor()
sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ({input('name : ')}, {input('id : ')})"
print(sql)
curs.execute(sql)
conn.commit()
conn.close()
#
#-----------------------------------------------------------------------------
# put

# curs = conn.cursor()
# sql = f"UPDATE bus SET bus_name={input('name : ')} WHERE bus_name={input('id : ')}"
# curs.execute(sql)
# conn.commit()
# conn.close()

#-----------------------------------------------------------------------------
# delete

# curs = conn.cursor()
# sql = f"DELETE FROM bus WHERE bus_name={input('버스이름 : ')}"
# curs.execute(sql)
# conn.commit()
#
# conn.close()

