import requests, xmltodict
from dotenv import load_dotenv
from api_bus import getBusAll
import os

load_dotenv()
key = os.getenv('key')


# 특정 노선의 버스 조회
def getBusInfo():
    url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={input('bus_id : ')}"
    content = requests.get(url).content
    dict = xmltodict.parse(content)
    data = dict['ServiceResult']['msgBody']['itemList']
    bus_list = []
    for i in range(len(data)):
        bus_dict = {}
        vehid = data[i]['vehId']
        plainno = data[i]['plainNo']
        gpsx = data[i]['gpsX']
        gpsy = data[i]['gpsY']

        bus_dict['vehId'] = vehid
        bus_dict['plainNo'] = plainno
        bus_dict['gpsX'] = gpsx
        bus_dict['gpsY'] = gpsy
        bus_list.append(bus_dict)
        # print(f"버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")
    return bus_list



def getBusInfoAll():
    buslist = getBusAll()
    bus_list = []
    for bus in buslist:
        url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={bus['bus_id']}"
        content = requests.get(url).content  # GET요청
        dict = xmltodict.parse(content)  # XML을 dictionary로 파싱
        data = dict['ServiceResult']['msgBody']['itemList']

        for veh in range(len(data)):
            bus_dict = {}
            busid = bus['bus_id']
            vehid = data[veh]['vehId']
            plainno = data[veh]['plainNo']
            gpsx = data[veh]['gpsX']
            gpsy = data[veh]['gpsY']

            bus_dict['bus_id'] = busid
            bus_dict['vehId'] = vehid
            bus_dict['plainNo'] = plainno
            bus_dict['gpsX'] = gpsx
            bus_dict['gpsY'] = gpsy
            bus_list.append(bus_dict)
    return bus_list

