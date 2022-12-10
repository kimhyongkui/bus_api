import requests, xmltodict
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

# 노선ID로 차량들의 위치정보 조회 (심야엔 버스가 운행을 정지하기에 조회가 안되는듯)
# url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={input('bus_id : ')}"
url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId=102900004"


content = requests.get(url).content
dict = xmltodict.parse(content)
data = dict['ServiceResult']['msgBody']['itemList']


def getBusInfo():
    bus_list = []
    for bus in range(len(data)):
        bus_dict = {}
        vehid = data[bus]['vehId']
        plainno = data[bus]['plainNo']
        gpsx = data[bus]['gpsX']
        gpsy = data[bus]['gpsY']

        bus_dict['vehId'] = vehid
        bus_dict['plainNo'] = plainno
        bus_dict['gpsX'] = gpsx
        bus_dict['gpsY'] = gpsy
        bus_list.append(bus_dict)
        print(f"버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {gpsx[0:9]} / {gpsy[0:9]}")
    return bus_list


