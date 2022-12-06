import requests, xmltodict
from dotenv import load_dotenv
import os
from api_bus import getBusAll

load_dotenv()
key = os.getenv('key')

buslist = getBusAll()

def geturl():
    station_list = []
    for bus in buslist:
        busid = bus['bus_id']
        url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={busid}"
        content = requests.get(url).content  # GET요청
        dict = xmltodict.parse(content)  # XML을 dictionary로 파싱
        data = dict['ServiceResult']['msgBody']['itemList']
        for station in range(len(data)) :
            station_dict = {}
            station_id = data[station]['station']
            station_name = data[station]['stationNm']
            station_no = data[station]['stationNo']
            station_gpsx = data[station]['gpsX']
            station_gpsy = data[station]['gpsY']

            station_dict['station'] = station_id
            station_dict['stationNm'] = station_name
            station_dict['stationNo'] = station_no
            station_dict['gpsX'] = station_gpsx
            station_dict['gpsY'] = station_gpsy
            station_list.append(station_dict)
            print(station_dict)
    return station_list







