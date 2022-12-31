import requests, json
from geopy.geocoders import Nominatim
from api_station import get_stn_list

# 현재위치
# lat = gpsX / lng = gpsY
# def current_location():
#     here_req = requests.get("http://www.geoplugin.net/json.gp")
#
#     if (here_req.status_code != 200):
#         print("현재좌표를 불러올 수 없음")
#     else:
#         location = json.loads(here_req.text)
#         crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}
#         print(crd['lat'], crd['lng'])
#     return crd
#
#
# current_location()



# 지오코딩 : 지역이름 적으면 좌표나오는거
# lat = gpsX / lng = gpsY
def geocoding(address):
    geolocoder = Nominatim(user_agent='South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    print(crd)

    return crd





# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_station_list(crd):
    crd = geocoding(crd)
    abc = get_stn_list(crd['lng'], crd['lat'], 100)
    data_list = []
    for i in range(len(abc)):
        data_dict = {}
        data_dict['stnId'] = abc[i]['stnId']
        data_dict['stnNm'] = abc[i]['stnNm']
        data_dict['arsId'] = abc[i]['arsId']
        data_list.append(data_dict)
        print(data_dict)
    return abc

get_station_list('노량진역')