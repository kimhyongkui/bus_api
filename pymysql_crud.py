from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')




# get(n번째)
# try:
#     curs = conn.cursor()
#     sql = "SELECT * FROM bus"
#     curs.execute(sql)
#     data = curs.fetchall()
#     print(data[0])
#
# finally:
#     conn.close()



# get(특정)
# try:
#     val = 6002
#     curs = conn.cursor()
#     sql = f"SELECT * FROM bus WHERE bus_name={val}"
#     curs.execute(sql)
#     result = curs.fetchall()
#     conn.commit()
#
#     for i in result:
#         print(i)
#
# finally:
#     conn.close()


# get(전체)
# try:
#     curs = conn.cursor()
#     sql = "SELECT * FROM bus"
#     curs.execute(sql)
#     result = curs.fetchall()
#     conn.commit()
#
#     for i in result:
#         print(i)
#
# finally:
#     conn.close()

# post
# try:
#     curs = conn.cursor()
#     getBusAll()
#     bus_list = getBusAll()
#     bus_name = bus_list[0::2]
#     bus_id = bus_list[1::2]
#
#     for i in range(len(bus_list)):
#         i = i+1
#         sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ({bus_name[i-1]}, {bus_id[i-1]})"
#         curs.execute(sql)
#         conn.commit()
# finally:
#     conn.close()
#
# put
# try:
#     val1 = 6001
#     val2 = 6002
#     curs = conn.cursor()
#     sql = f"UPDATE bus SET bus_name={val1} WHERE bus_name={val2}"
#     curs.execute(sql)
#     conn.commit()
#
# finally:
#     conn.close()


# delete
# try:
#     val = ("6001")
#     curs = conn.cursor()
#     sql = f"DELETE FROM bus WHERE bus_name={val}"
#     curs.execute(sql)
#     conn.commit()
#
# finally:
#     conn.close()
