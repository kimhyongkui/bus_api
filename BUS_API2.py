import requests, xmltodict, json
from dotenv import load_dotenv
import os
import pymysql


load_dotenv()
key = os.getenv('key')
# key = os.environ.get('key') getenv가 좀더 간결한 코드로 같은 효과

url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}"
# f-string을 이용해서 포매팅


content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱

jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString) # JSON 디코딩, json을 dict으로 변환

def getBusRouteId(bus_number):
    bus_number = str(bus_number)
    bus_dict = {}
    for bus in jsonObj:
        bus_name = bus['busRouteNm']
        bus_Id = bus['busRouteId']
        bus_dict[bus_name] = bus_Id
        if bus_number == bus_name:
            print(f'{bus_name}의 버스ID는 {bus_Id}입니다.')


getBusRouteId(6001)

def db_insert(bus_dict):
    db = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd=os.getenv('user_pwd'),
                           db='127.0.0.1',
                           charset='utf8')
    cursor = db.cursor()

    sql = "INSERT INTO bus(bus_name,bus_id) values(%s, %s)"
    cursor.execute(sql, bus_dict)
    db.commit()
    db.close()

