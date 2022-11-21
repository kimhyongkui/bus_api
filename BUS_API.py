import requests, xmltodict, json
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv('key')
# key = os.environ.get('key')

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
            break

getBusRouteId(6001)



