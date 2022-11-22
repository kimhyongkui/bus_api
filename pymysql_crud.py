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
#     curs = conn.cursor()
#     sql = "SELECT * FROM bus WHERE bus_name=%s"
#     val = ("6001")
#     curs.execute(sql, val)
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
#     sql = "SELECT * FROM bus WHERE bus_name=%s"
#     val = ("6001")
#     curs.execute(sql, val)
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
#     sql = "INSERT INTO bus VALUES (%s, %s)"
#     val = (6003, 120003)
#     curs.execute(sql, val)
#     conn.commit()
#
# finally:
#     conn.close()


# put
try:
    curs = conn.cursor()
    sql = "UPDATE bus SET bus_name=%s WHERE bus_name=%s"
    val = ("6001", "6002")
    curs.execute(sql, val)
    conn.commit()

finally:
    conn.close()


# delete
# try:
#     curs = conn.cursor()
#     sql = "DELETE FROM bus WHERE bus_name=%s"
#     val = ("6001")
#     curs.execute(sql, val)
#     conn.commit()
#
# finally:
#     conn.close()
