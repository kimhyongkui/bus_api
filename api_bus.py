import requests, xmltodict
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

# 노선번호에 해당하는 노선 목록 조회
url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}"

content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱

data = dict['ServiceResult']['msgBody']['itemList']



def getBusAll():
    bus_list = []
    for i in range(len(data)):
        bus_dict = {}
        bus_name = data[i]["busRouteNm"]
        bus_Id = data[i]["busRouteId"]
        bus_dict["bus_name"] = bus_name
        bus_dict["bus_id"] = bus_Id
        bus_list.append(bus_dict)
        print(bus_dict)
    return bus_list

getBusAll()