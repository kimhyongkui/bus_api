import requests, xmltodict
from dotenv import load_dotenv
import os


load_dotenv()
key = os.getenv('key')


# url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId={input('bus_id : ')}"
url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?serviceKey={key}&busRouteId=100100416"


content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱
data = dict['ServiceResult']['msgBody']['itemList']


def getStationAll():
    station_list = []
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

    return station_list



# def getbusrouteid():
#     busid_list = getBusID()
#     # for id in range(len(bus_list)):
#     #     bus_id = busid_list[id]['bus_id']
#     print(busid_list)

