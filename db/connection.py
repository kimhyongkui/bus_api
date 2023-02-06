from dotenv import load_dotenv
import pymysql
import os

load_dotenv()
key = os.getenv('key')

conn = pymysql.connect(host='127.0.0.1', user='root',
                       password=os.getenv('user_pwd'), db='prac', charset='utf8')
