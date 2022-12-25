import requests
import xmltodict
from dotenv import load_dotenv
from api_route import get_route_all
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
            vehid = data_list[bus]['vehId']  # 버스 Id
            plainno = data_list[bus]['plainNo']  # 차량번호
            gpsx = data_list[bus]['gpsX']
            gpsy = data_list[bus]['gpsY']

            bus_dict['routeid'] = routeid
            bus_dict['vehId'] = vehid
            bus_dict['plainNo'] = plainno
            bus_dict['gpsX'] = gpsx
            bus_dict['gpsY'] = gpsy
            bus_list.append(bus_dict)
            print(f"버스노선고유번호 : {routeid}, 버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")

    elif isinstance(data['itemList'], list):
        for bus in range(len(data['itemList'])):
            bus_dict = {}
            vehid = data['itemList'][bus]['vehId']
            plainno = data['itemList'][bus]['plainNo']
            gpsx = data['itemList'][bus]['gpsX']
            gpsy = data['itemList'][bus]['gpsY']

            bus_dict['bus_id'] = routeid
            bus_dict['vehId'] = vehid
            bus_dict['plainNo'] = plainno
            bus_dict['gpsX'] = gpsx
            bus_dict['gpsY'] = gpsy
            bus_list.append(bus_dict)
            print(f"버스노선고유번호 : {routeid}, 버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")

    return bus_list


# 전체 노선의 버스 조회
def get_bus_info_all():
    route_list = get_route_all()
    bus_list = []
    for bus in route_list:
        routeid = bus['bus_id']
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
                vehid = data_list[bus]['vehId']
                plainno = data_list[bus]['plainNo']
                gpsx = data_list[bus]['gpsX']
                gpsy = data_list[bus]['gpsY']

                bus_dict['bus_id'] = routeid
                bus_dict['vehId'] = vehid
                bus_dict['plainNo'] = plainno
                bus_dict['gpsX'] = gpsx
                bus_dict['gpsY'] = gpsy
                bus_list.append(bus_dict)
                print(f"버스노선고유번호 : {routeid}, 버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")

        elif isinstance(data['itemList'], list):
            for bus in range(len(data['itemList'])):
                bus_dict = {}
                vehid = data['itemList'][bus]['vehId']
                plainno = data['itemList'][bus]['plainNo']
                gpsx = data['itemList'][bus]['gpsX']
                gpsy = data['itemList'][bus]['gpsY']

                bus_dict['bus_id'] = routeid
                bus_dict['vehId'] = vehid
                bus_dict['plainNo'] = plainno
                bus_dict['gpsX'] = gpsx
                bus_dict['gpsY'] = gpsy
                bus_list.append(bus_dict)
                print(f"버스노선고유번호 : {routeid}, 버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")
    return bus_list
