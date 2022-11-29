import requests, xmltodict, json
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')


url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={input('bus_id : ')}"

content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString)

def getStationAll():
    for station in jsonObj :
        print(station['stationNm'])

        bus_dict = []
        bus_station = jsonObj[i]['stationNm']
        bus_Id = jsonObj[i]["busRouteId"]
        bus_dict["bus_name"] = bus_name
        bus_dict["bus_id"] = bus_Id
        bus_list.append(bus_dict)
    return bus_list
