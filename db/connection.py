from dotenv import load_dotenv
from pymysqlpool.pool import Pool
import os

load_dotenv()

conn = Pool(host='127.0.0.1',
            user='root',
            password=os.getenv('user_pwd'),
            db='prac',
            charset='utf8'
            )
