import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.api_route import get_route_all

load_dotenv()
key = os.getenv('key')


# 특정 노선의 경유 정류소 데이터 얻기
def get_station(routeid):
    url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
          f"serviceKey={key}&busRouteId={routeid}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    stn_list = []
    for station in range(len(data)):
        stn_dict = {'routeId': routeid,
                    'routeNm': data[station]['busRouteNm'],
                    'routeAbrv': data[station]['busRouteAbrv'],
                    'stnId': data[station]['station'],
                    'stnNm': data[station]['stationNm'],
                    'arsId': data[station]['arsId'],
                    'direction': data[station]['direction'],
                    'gpsX': data[station]['gpsX'],
                    'gpsY': data[station]['gpsY']
                    }
        stn_list.append(stn_dict)
        print(stn_dict)
    return stn_list


# 모든 정류소 데이터 얻기
def get_station_all():
    route_list = get_route_all()
    stn_list = []
    for route in route_list:
        routeid = route['routeId']
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
              f"serviceKey={key}&busRouteId={routeid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        for station in range(len(data)):
            stn_dict = {'routeId': routeid,
                        'routeNm': data[station]['busRouteNm'],
                        'routeAbrv': data[station]['busRouteAbrv'],
                        'stnId': data[station]['station'],
                        'stnNm': data[station]['stationNm'],
                        'arsId': data[station]['arsId'],
                        'direction': data[station]['direction'],
                        'gpsX': data[station]['gpsX'],
                        'gpsY': data[station]['gpsY']
                        }
            stn_list.append(stn_dict)
            print(stn_dict)
    return stn_list


# 특정 좌표 인근 정류소 데이터 얻기
def get_stn_list(gpsx, gpsy, radius):
    url = f"http://ws.bus.go.kr/api/rest/stationinfo/getStationByPos?" \
          f"serviceKey={key}&tmX={gpsx}&tmY={gpsy}&radius={radius}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']
    stn_list = []
    if data is None:
        print('정류소가 없습니다')
    elif isinstance(data['itemList'], dict):
        stn_dict = {'stnId': data['itemList']['stationId'],
                    'stnNm': data['itemList']['stationNm'],
                    'arsId': data['itemList']['arsId'],
                    'gpsX': data['itemList']['gpsX'],
                    'gpsY': data['itemList']['gpsY'],
                    'dist': data['itemList']['dist']
                    }
        stn_list.append(stn_dict)
    else:
        data_list = data['itemList']
        for station in range(len(data_list)):
            stn_dict = {'stnId': data_list[station]['stationId'],
                        'stnNm': data_list[station]['stationNm'],
                        'arsId': data_list[station]['arsId'],
                        'gpsX': data_list[station]['gpsX'],
                        'gpsY': data_list[station]['gpsY'],
                        'dist': data_list[station]['dist']
                        }
            stn_list.append(stn_dict)
    return stn_list
