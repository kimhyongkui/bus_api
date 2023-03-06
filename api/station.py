import requests
import xmltodict
from dotenv import load_dotenv
import os
from api.route import get_all_route_list

load_dotenv()


# 특정 노선의 경유 정류소 데이터 얻기
def get_station_data(route_id):
    try:
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?" \
              f"serviceKey={os.getenv('key')}&busRouteId={route_id}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']['itemList']
        stn_list = []
        for station in data:
            stn_dict = {
                'routeId': route_id,
                'routeNm': station['busRouteNm'],
                'routeAbrv': station['busRouteAbrv'],
                'stnId': station['station'],
                'stnNm': station['stationNm'],
                'arsId': station['arsId'],
                'direction': station['direction'],
                'gpsX': station['gpsX'],
                'gpsY': station['gpsY']
            }
            stn_list.append(stn_dict)
        return stn_list

    except Exception as err:
        return f"{err}, 노선 ID를 확인하세요"


# 모든 정류소 데이터 얻기
def get_all_station_data():
    try:
        stn_data_list = []
        for route_id in get_all_route_list():
            data = get_station_data(route_id['routeId'])
            stn_data_list.extend(data)
        return stn_data_list

    except Exception as err:
        return f"{err}, 노선 ID를 확인하세요"
