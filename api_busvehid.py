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

jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

def getBusInfo():
    bus_list = []
    for i in range(len(jsonObj)):
        bus_dict = {}
        vehid = jsonObj[i]["vehId"]
        plainno = jsonObj[i]["plainNo"]
        posx = jsonObj[i]["posX"]
        posy = jsonObj[i]["posY"]

        bus_dict["vehId"] = vehid
        bus_dict["plainNo"] = plainno
        bus_dict["posX"] = posx
        bus_dict["posY"] = posy
        bus_list.append(bus_dict)
        print("버스고유번호 :", vehid, "버스이름 :", plainno, "버스좌표 :", posx, posy)

    return bus_list


