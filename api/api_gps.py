import requests, json
from geopy.geocoders import Nominatim

# 현재위치
def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")
    global current_gps

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        current_gps = {"gpsY": str(location["geoplugin_latitude"]), "gpsX": str(location["geoplugin_longitude"])}

    return current_gps


# 지오코딩 : 지역이름 적으면 좌표나오는거
def geocoding(address):
    geolocoder = Nominatim(user_agent='South Korea')
    geo = geolocoder.geocode(address)
    gps = {"gpsY": str(geo.latitude), "gpsX": str(geo.longitude)}

    return gps

