from bus_api import getBusAll
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')




curs = conn.cursor()

bus_list = getBusAll()

# for bus_data in bus_list:
#
#     data = {'val1': bus_data["bus_name"], 'val2' : bus_data["bus_id"]}
#     sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{data['val1']}', {data['val2']})"
#     curs.execute(sql)
#     conn.commit()
#
# print("DB 저장 완료")
# conn.close()


for bus_data in bus_list:

    sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{bus_data['bus_name']}', {bus_data['bus_id']})"
    curs.execute(sql)
    conn.commit()

print("DB 저장 완료")
conn.close()



