import requests
import xmltodict
from dotenv import load_dotenv
from api.route import get_route_all
from db.get.db_data import get_route_data
import os

load_dotenv()


# 특정 노선의 버스 조회
def get_bus_info(routeNm):
    try:
        routeid = get_route_data(routeNm)
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
              f"serviceKey={os.getenv('key')}&busRouteId={routeid['routeId']}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']
        bus_list = []
        if not data:
            bus_list = '데이터가 없습니다'

        elif isinstance(data['itemList'], dict):
            bus_dict = {
                'routeId': routeid['routeId'],
                'vehId': data['itemList']['vehId'],
                'plainNo': data['itemList']['plainNo'],
                'gpsX': data['itemList']['gpsX'],
                'gpsY': data['itemList']['gpsY']
            }
            bus_list.append(bus_dict)

        elif isinstance(data['itemList'], list):
            for bus in data['itemList']:
                bus_dict = {
                    'routeId': routeid['routeId'],
                    'vehId': bus['vehId'],
                    'plainNo': bus['plainNo'],
                    'gpsX': bus['gpsX'],
                    'gpsY': bus['gpsY']
                }
                bus_list.append(bus_dict)

        return bus_list

    except Exception as err:
        return f"{err}, 노선 이름을 확인하세요"


# 전체 노선의 버스 조회
def get_bus_info_all():
    try:
        route_list = get_route_all()
        bus_list = []
        for route_data in route_list:
            routeid = route_data['routeId']
            url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
                  f"serviceKey={os.getenv('key')}&busRouteId={routeid}"
            content = requests.get(url).content
            xmldict = xmltodict.parse(content)
            data = xmldict['ServiceResult']['msgBody']
            if not data:
                print(f"{routeid}번 노선의 데이터가 없습니다")
                continue

            elif isinstance(data['itemList'], dict):
                bus_dict = {
                    'routeId': routeid,
                    'vehId': data['itemList']['vehId'],
                    'plainNo': data['itemList']['plainNo'],
                    'gpsX': data['itemList']['gpsX'],
                    'gpsY': data['itemList']['gpsY']
                }
                bus_list.append(bus_dict)
                print(f"{routeid}번 노선의 데이터를 추가했습니다")

            elif isinstance(data['itemList'], list):
                for bus in data['itemList']:
                    bus_dict = {
                        'routeId': routeid,
                        'vehId': bus['vehId'],
                        'plainNo': bus['plainNo'],
                        'gpsX': bus['gpsX'],
                        'gpsY': bus['gpsY']
                    }
                    bus_list.append(bus_dict)
                print(f"{routeid}번 노선의 데이터를 추가했습니다")

        return bus_list

    except Exception as err:
        return f"{err}, 노선 이름을 확인하세요"
