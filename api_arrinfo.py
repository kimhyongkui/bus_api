import requests, xmltodict
from dotenv import load_dotenv
import os
from api_bus import get_busall


load_dotenv()
key = os.getenv('key')

# 특정 경유노선의 전체정류소 데이터 얻기
def get_arrive_info(busid):
    url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={key}&busRouteId={busid}"
    content = requests.get(url).content  # GET요청
    dict = xmltodict.parse(content)  # XML을 dictionary로 파싱
    data = dict['ServiceResult']['msgBody']['itemList']
    arrive_list = []
    for arrive in range(len(data)) :
        arrive_dict = {}
        arrive_id = busid
        arrive_busnm = data[arrive]['rtNm']
        arrive_ord = data[arrive]['staOrd']
        arrive_stnm = data[arrive]['stNm']

        arrive_dict['bus_id'] = arrive_id
        arrive_dict['rtNm'] = arrive_busnm
        arrive_dict['staOrd'] = arrive_ord
        arrive_dict['stNm'] = arrive_stnm
        arrive_list.append(arrive_dict)
        print(arrive_dict)
    return arrive_list



# 모든 경유노선의 전체정류소 데이터 얻기
def get_arrive_infoall():
    buslist = get_busall()
    arrive_list = []
    for bus in buslist:
        busid = bus['bus_id']
        url = f"http://ws.bus.go.kr/api/rest/arrive/getArrInfoByRouteAll?serviceKey={key}&busRouteId={busid}"
        content = requests.get(url).content  # GET요청
        dict = xmltodict.parse(content)  # XML을 dictionary로 파싱
        data = dict['ServiceResult']['msgBody']['itemList']
        for arrive in range(len(data)) :
            arrive_dict = {}
            arrive_id = busid
            arrive_busnm = data[arrive]['rtNm']
            arrive_ord = data[arrive]['staOrd']
            arrive_stnm = data[arrive]['stNm']

            arrive_dict['bus_id'] = arrive_id
            arrive_dict['rtNm'] = arrive_busnm
            arrive_dict['staOrd'] = arrive_ord
            arrive_dict['stNm'] = arrive_stnm
            arrive_list.append(arrive_dict)
            print(arrive_dict)
    return arrive_list



