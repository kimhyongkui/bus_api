import requests
import xmltodict
from dotenv import load_dotenv
from api.api_route import get_route_all
from db.db_get_data import get_route_name
import os

load_dotenv()


# 특정 노선의 버스 조회
def get_bus_info(routeNm):
    routeid = get_route_name(routeNm)
    url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={os.getenv('key')}&busRouteId={routeid}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']
    bus_list = []

    if data is None:
        print('데이터가 없습니다')

    elif isinstance(data['itemList'], dict):
        data_list = [data['itemList']]
        for bus in range(len(data_list)):
            bus_dict = {'routeid': routeid,
                        'vehId': data_list[bus]['vehId'],
                        'plainNo': data_list[bus]['plainNo'],
                        'gpsX': data_list[bus]['gpsX'],
                        'gpsY': data_list[bus]['gpsY']
                        }

            bus_list.append(bus_dict)

    elif isinstance(data['itemList'], list):
        for bus in range(len(data['itemList'])):
            bus_dict = {'routeId': routeid,
                        'vehId': data['itemList'][bus]['vehId'],
                        'plainNo': data['itemList'][bus]['plainNo'],
                        'gpsX': data['itemList'][bus]['gpsX'],
                        'gpsY': data['itemList'][bus]['gpsY']
                        }
            bus_list.append(bus_dict)

    return bus_list


# 전체 노선의 버스 조회
def get_bus_info_all():
    route_list = get_route_all()
    bus_list = []
    for bus in route_list:
        routeid = bus['routeId']
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={os.getenv('key')}&busRouteId={routeid}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']

        if data is None:
            print('데이터가 없습니다')

        elif isinstance(data['itemList'], dict):
            data_list = [data['itemList']]
            for bus in range(len(data_list)):
                bus_dict = {'routeId': routeid,
                            'vehId': data_list[bus]['vehId'],
                            'plainNo': data_list[bus]['plainNo'],
                            'gpsX': data_list[bus]['gpsX'],
                            'gpsY': data_list[bus]['gpsY']
                            }

                bus_list.append(bus_dict)

        elif isinstance(data['itemList'], list):
            for bus in range(len(data['itemList'])):
                bus_dict = {'routeId': routeid,
                            'vehId': data['itemList'][bus]['vehId'],
                            'plainNo': data['itemList'][bus]['plainNo'],
                            'gpsX': data['itemList'][bus]['gpsX'],
                            'gpsY': data['itemList'][bus]['gpsY']
                            }

                bus_list.append(bus_dict)

    return bus_list
