import requests, xmltodict
from dotenv import load_dotenv
import os
from api_route import get_route_all


load_dotenv()
key = os.getenv('key')

# 특정 노선의 경유 정류소 데이터 얻기

def get_station(route_id):
    url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={route_id}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    stn_list = []
    for station in range(len(data)):
        stn_dict = {}
        route_name = data[station]['busRouteNm'] # 노선명
        route_abrv = data[station]['busRouteAbrv']  # 노선명
        stn_id = data[station]['station'] #정류소 ID
        stn_name = data[station]['stationNm'] #정류소 이름
        stn_no = data[station]['arsId'] #정류소 고유번호
        stn_dir = data[station]['direction'] #진행방향
        stn_gpsx = data[station]['gpsX'] #정류소 좌표
        stn_gpsy = data[station]['gpsY'] #정류소 좌표

        stn_dict['routeId'] = route_id
        stn_dict['busRouteNm'] = route_name
        stn_dict['busRouteAbrv'] = route_abrv
        stn_dict['station'] = stn_id
        stn_dict['stationNm'] = stn_name
        stn_dict['arsId'] = stn_no
        stn_dict['direction'] = stn_dir
        stn_dict['gpsX'] = stn_gpsx
        stn_dict['gpsY'] = stn_gpsy
        stn_list.append(stn_dict)
    return stn_list



# 모든 정류소 데이터 얻기
def get_station_all():
    route_list = get_route_all()
    stn_list = []
    for route in route_list:
        route_id = route['routeId']
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={route_id}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for station in range(len(data)):
            stn_dict = {}
            route_name = data[station]['busRouteNm']  # 노선명
            route_abrv = data[station]['busRouteAbrv']  # 노선명
            stn_id = data[station]['station']  # 정류소 ID
            stn_name = data[station]['stationNm']  # 정류소 이름
            stn_no = data[station]['arsId']  # 정류소 고유번호
            stn_dir = data[station]['direction']  # 진행방향
            stn_gpsx = data[station]['gpsX']  # 정류소 좌표
            stn_gpsy = data[station]['gpsY']  # 정류소 좌표

            stn_dict['routeId'] = route_id
            stn_dict['busRouteNm'] = route_name
            stn_dict['busRouteAbrv'] = route_abrv
            stn_dict['station'] = stn_id
            stn_dict['stationNm'] = stn_name
            stn_dict['arsId'] = stn_no
            stn_dict['direction'] = stn_dir
            stn_dict['gpsX'] = stn_gpsx
            stn_dict['gpsY'] = stn_gpsy
            stn_list.append(stn_dict)

    return stn_list


# 특정 좌표 인근 정류소 데이터 얻기
def get_stn_list(tmx, tmy, radius):
    url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?serviceKey={key}&tmX={tmx}&tmY={tmy}&radius={radius}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    stn_list = []
    for station in range(len(data)):
        stn_dict = {}
        stn_id = data[station]['stationId']
        stn_name = data[station]['stationNm']
        stn_no = data[station]['arsId']
        stn_gpsx = data[station]['gpsX']
        stn_gpsy = data[station]['gpsY']
        stn_dist = data[station]['dist']

        stn_dict['stationId'] = stn_id
        stn_dict['stationNm'] = stn_name
        stn_dict['arsId'] = stn_no
        stn_dict['gpsX'] = stn_gpsx
        stn_dict['gpsY'] = stn_gpsy
        stn_dict['dist'] = stn_dist
        stn_list.append(stn_dict)
        print(stn_dict)
    return stn_list

