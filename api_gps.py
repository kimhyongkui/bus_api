import requests, json
from geopy.geocoders import Nominatim
from api_station import get_stn_list

# 현재위치
# lat = gpsX / lng = gpsY
def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        crd = {"lat": str(location["geoplugin_latitude"]), "lng": str(location["geoplugin_longitude"])}
        print(crd['lat'], crd['lng'])
    return crd


current_location()



# 지오코딩 : 지역이름 적으면 좌표나오는거
# lat = gpsX / lng = gpsY
def geocoding(address):
    geolocoder = Nominatim(user_agent='South Korea', timeout=None)
    geo = geolocoder.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}
    print(crd)

    return crd

geocoding("봉천역")



# # 특정 지역 좌표 입력해서 인근 정류소 구해보기
# def get_station_list():
#     get_stn_list(crd['lng'], crd['lat'], 500)
#
# print(get_station_list())