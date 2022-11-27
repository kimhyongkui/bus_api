from fastapi import FastAPI
from bus_api import getBusAll
from dotenv import load_dotenv
import pymysql
import os


load_dotenv()

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')

app = FastAPI()



curs = conn.cursor()
bus_list = getBusAll()


for bus_data in bus_list:
    val1 = bus_data["bus_name"]
    val2 = bus_data["bus_id"]

    sql = f"INSERT INTO bus (bus_name, bus_id) VALUES ('{val1}', {val2})"
    curs.execute(sql)
    conn.commit()
conn.close()
