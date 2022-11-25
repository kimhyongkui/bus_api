from fastapi import FastAPI
from bus_api import getBusAll
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')

app = FastAPI()


try:
    curs = conn.cursor()
    getBusAll()
    bus_list = getBusAll()
    bus_name = bus_list[0::2]
    bus_id = bus_list[1::2]

    for i in range(len(bus_list)):
        i = i+1
        sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ({bus_name[i]}, {bus_id[i]})"
        curs.execute(sql)
        conn.commit()
finally:
    conn.close()
