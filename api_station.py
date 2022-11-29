import requests, xmltodict, json
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')


# url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={input('bus_id : ')}"
url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId=100100412"

content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString)

def getStationAll():
    station_list = []
    for i in range(len(jsonObj)) :
        bus_station = jsonObj[i]['stationNm']
        station_list.append(bus_station)
    return station_list

