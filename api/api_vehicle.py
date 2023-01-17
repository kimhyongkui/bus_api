import requests
import xmltodict
from dotenv import load_dotenv
from api.api_route import get_route_all
import os

load_dotenv()
key = os.getenv('key')


# 특정 노선의 버스 조회
def get_bus_info(routeid):
    url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={routeid}"
    content = requests.get(url).content
    xmldict = xmltodict.parse(content)
    data = xmldict['ServiceResult']['msgBody']
    bus_list = []

    if data is None:
        print('데이터가 없습니다')

    elif isinstance(data['itemList'], dict):
        data_list = []
        data_list.append(data['itemList'])
        for bus in range(len(data_list)):
            bus_dict = {}
            bus_dict['routeid'] = routeid
            bus_dict['vehId'] = data_list[bus]['vehId']  # 버스 Id
            bus_dict['plainNo'] = data_list[bus]['plainNo']  # 차량번호
            bus_dict['gpsX'] = data_list[bus]['gpsX']
            bus_dict['gpsY'] = data_list[bus]['gpsY']

            bus_list.append(bus_dict)

    elif isinstance(data['itemList'], list):
        for bus in range(len(data['itemList'])):
            bus_dict = {}

            bus_dict['routeId'] = routeid
            bus_dict['vehId'] = data['itemList'][bus]['vehId']
            bus_dict['plainNo'] = data['itemList'][bus]['plainNo']
            bus_dict['gpsX'] = data['itemList'][bus]['gpsX']
            bus_dict['gpsY'] = data['itemList'][bus]['gpsY']
            bus_list.append(bus_dict)

    return bus_list


# 전체 노선의 버스 조회
def get_bus_info_all():
    route_list = get_route_all()
    bus_list = []
    for bus in route_list:
        routeid = bus['routeId']
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={routeid}"
        content = requests.get(url).content
        xmldict = xmltodict.parse(content)
        data = xmldict['ServiceResult']['msgBody']

        if data is None:
            print('데이터가 없습니다')

        elif isinstance(data['itemList'], dict):
            data_list = []
            data_list.append(data['itemList'])
            for bus in range(len(data_list)):
                bus_dict = {}

                bus_dict['routeId'] = routeid
                bus_dict['vehId'] = data_list[bus]['vehId']
                bus_dict['plainNo'] = data_list[bus]['plainNo']
                bus_dict['gpsX'] = data_list[bus]['gpsX']
                bus_dict['gpsY'] = data_list[bus]['gpsY']
                bus_list.append(bus_dict)

        elif isinstance(data['itemList'], list):
            for bus in range(len(data['itemList'])):
                bus_dict = {}

                bus_dict['routeId'] = routeid
                bus_dict['vehId'] = data['itemList'][bus]['vehId']
                bus_dict['plainNo'] = data['itemList'][bus]['plainNo']
                bus_dict['gpsX'] = data['itemList'][bus]['gpsX']
                bus_dict['gpsY'] = data['itemList'][bus]['gpsY']
                bus_list.append(bus_dict)

    return bus_list
