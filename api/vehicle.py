import requests
import xmltodict
from dotenv import load_dotenv
from api.route import get_all_route_list
from db.get.db_data import get_route_list
import os

load_dotenv()


# 특정 노선의 버스 조회
def get_vehicle_data(route_name):
    try:
        route_id = get_route_list(route_name)
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
              f"serviceKey={os.getenv('key')}&busRouteId={route_id['routeId']}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']
        vehicle_list = []
        if not data:
            vehicle_list = '데이터가 없습니다'

        elif isinstance(data['itemList'], dict):
            vehicle_dict = {
                'routeId': route_id['routeId'],
                'vehId': data['itemList']['vehId'],
                'plainNo': data['itemList']['plainNo'],
                'gpsX': data['itemList']['gpsX'],
                'gpsY': data['itemList']['gpsY']
            }
            vehicle_list.append(vehicle_dict)

        elif isinstance(data['itemList'], list):
            for bus in data['itemList']:
                vehicle_dict = {
                    'routeId': route_id['routeId'],
                    'vehId': bus['vehId'],
                    'plainNo': bus['plainNo'],
                    'gpsX': bus['gpsX'],
                    'gpsY': bus['gpsY']
                }
                vehicle_list.append(vehicle_dict)

        return vehicle_list

    except Exception as err:
        return f"{err}, 노선 이름을 확인하세요"


# 전체 노선의 버스 조회
def get_all_vehicle_data():
    try:
        route_list = get_all_route_list()
        vehicle_list = []
        for route_data in route_list:
            route_id = route_data['routeId']
            url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?" \
                  f"serviceKey={os.getenv('key')}&busRouteId={route_id}"
            content = requests.get(url).content
            xmldict = xmltodict.parse(content)
            data = xmldict['ServiceResult']['msgBody']
            if not data:
                print(f"{route_id}번 노선의 데이터가 없습니다")
                continue

            elif isinstance(data['itemList'], dict):
                vehicle_dict = {
                    'routeId': route_id,
                    'vehId': data['itemList']['vehId'],
                    'plainNo': data['itemList']['plainNo'],
                    'gpsX': data['itemList']['gpsX'],
                    'gpsY': data['itemList']['gpsY']
                }
                vehicle_list.append(vehicle_dict)
                print(f"{route_id}번 노선의 데이터를 추가했습니다")

            elif isinstance(data['itemList'], list):
                for vehicle in data['itemList']:
                    vehicle_dict = {
                        'routeId': route_id,
                        'vehId': vehicle['vehId'],
                        'plainNo': vehicle['plainNo'],
                        'gpsX': vehicle['gpsX'],
                        'gpsY': vehicle['gpsY']
                    }
                    vehicle_list.append(vehicle_dict)
                print(f"{route_id}번 노선의 데이터를 추가했습니다")

        return vehicle_list

    except Exception as err:
        return f"{err}, 노선 이름을 확인하세요"
