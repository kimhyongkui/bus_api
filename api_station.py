import requests, xmltodict
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')


# url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={input('bus_id : ')}"
url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId=100100412"

content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱
data = dict['ServiceResult']['msgBody']['itemList']


def getStationAll():
    station_list = []
    for i in range(len(data)) :
        bus_station = data[i]['stationNm']
        station_list.append(bus_station)

    return station_list

getStationAll()