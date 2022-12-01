import requests, xmltodict, json
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv('key')

# 노선ID로 차량들의 위치정보 조회
# url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId={input('bus_id : ')}"
url = f"http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey={key}&busRouteId=100100412"

content = requests.get(url).content
dict = xmltodict.parse(content)

data = dict['ServiceResult']['msgBody']['itemList']

def getBusInfo():
    bus_list = []
    for i in range(len(data)):
        bus_dict = {}
        vehid = data[i]["vehId"]
        plainno = data[i]["plainNo"]
        posx = data[i]["posX"]
        posy = data[i]["posY"]

        bus_dict["vehId"] = vehid
        bus_dict["plainNo"] = plainno
        bus_dict["posX"] = posx
        bus_dict["posY"] = posy
        bus_list.append(bus_dict)
        # print(f"버스고유번호 : {vehid}, 버스이름 : {plainno}, 버스좌표(x,y) : {posx[0:9]} / {posy[0:9]}")
    return bus_list


def busVehPlain():
    bus = getBusInfo()
    for i in bus:
        vehid = i['vehId']
        plainno = i['plainNo']
        print(vehid, plainno)


def posxy():
    bus = getBusInfo()
    for i in bus:
        posx = i['posX']
        posy = i['posY']
        print(posx, posy)





