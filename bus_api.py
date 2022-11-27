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



def getBusAll():
    bus_list = []
    for i in range(len(jsonObj)):
        bus_dict = {}
        bus_name = (jsonObj[i]["busRouteNm"])
        bus_Id = (jsonObj[i]["busRouteId"])
        bus_dict["bus_name"] = bus_name
        bus_dict["bus_id"] = bus_Id
        bus_list.append(bus_dict)
    return bus_list

getBusAll()