import requests, xmltodict
from dotenv import load_dotenv
import os
from api_bus import get_bus_all


load_dotenv()
key = os.getenv('key')

# 특정 노선의 정류소 데이터 얻기

def get_station(busid):
    url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={busid}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    station_list = []
    for station in range(len(data)) :
        station_dict = {}
        station_id = data[station]['station']
        station_name = data[station]['stationNm']
        station_no = data[station]['stationNo']
        station_gpsx = data[station]['gpsX']
        station_gpsy = data[station]['gpsY']

        station_dict['bus_id'] = busid
        station_dict['station'] = station_id
        station_dict['stationNm'] = station_name
        station_dict['stationNo'] = station_no
        station_dict['gpsX'] = station_gpsx
        station_dict['gpsY'] = station_gpsy
        station_list.append(station_dict)

    return station_list


# 모든 정류소 데이터 얻기
def get_station_all():
    bus_list = get_bus_all()
    station_list = []
    for bus in bus_list:
        busid = bus['bus_id']
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={busid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for station in range(len(data)):
            station_dict = {}
            station_id = data[station]['station']
            station_name = data[station]['stationNm']
            station_no = data[station]['stationNo']
            station_gpsx = data[station]['gpsX']
            station_gpsy = data[station]['gpsY']

            station_dict['bus_id'] = busid
            station_dict['station'] = station_id
            station_dict['stationNm'] = station_name
            station_dict['stationNo'] = station_no
            station_dict['gpsX'] = station_gpsx
            station_dict['gpsY'] = station_gpsy
            station_list.append(station_dict)
    return station_list

# 특정 좌표 인근 정류소 데이터 얻기
def get_station_list(tmx, tmy, radius):
    url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?serviceKey={key}&tmX={tmx}&tmY={tmy}&radius={radius}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    station_list = []
    for station in range(len(data)):
        station_dict = {}
        station_id = data[station]['stationId']
        station_name = data[station]['stationNm']
        station_no = data[station]['arsId']
        station_gpsx = data[station]['gpsX']
        station_gpsy = data[station]['gpsY']
        station_dist = data[station]['dist']

        station_dict['stationId'] = station_id
        station_dict['stationNm'] = station_name
        station_dict['arsId'] = station_no
        station_dict['gpsX'] = station_gpsx
        station_dict['gpsY'] = station_gpsy
        station_dict['dist'] = station_dist
        station_list.append(station_dict)
        print(station_dict)
    return station_list

get_station_list(126.9433, 37.48235, 150)