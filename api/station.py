import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.route import get_route_all

load_dotenv()


# 특정 노선의 경유 정류소 데이터 얻기
def get_station(routeid):
    try:
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
              f"serviceKey={os.getenv('key')}&busRouteId={routeid}"
        content = requests.get(url).content
        dict = xmltodict.parse(content)
        data = dict['ServiceResult']['msgBody']['itemList']
        stn_list = []
        for station in range(len(data)):
            stn_dict = {
                'routeId': routeid,
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
        return stn_list

    except TypeError as err:
        return f"{err}, 노선 ID를 확인하세요"


# 모든 정류소 데이터 얻기
def get_station_all():
    try:
        route_list = get_route_all()
        stn_list = []
        for route in route_list:
            routeid = route['routeId']
            url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
                  f"serviceKey={os.getenv('key')}&busRouteId={routeid}"
            content = requests.get(url).content
            dict = xmltodict.parse(content)
            data = dict['ServiceResult']['msgBody']['itemList']
            for station in range(len(data)):
                stn_dict = {
                    'routeId': routeid,
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
        return stn_list

    except Exception:
        return 'Error'
