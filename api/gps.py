import requests
import json
from geopy.geocoders import Nominatim


# 지오코딩 : 지역이름 적으면 좌표나오는거
def specific_location(address):
    try:
        location = Nominatim(user_agent='South Korea')
        geo = location.geocode(address)
        if geo is None:
            gps = {"gpsY": "null", "gpsX": "null"}
        else:
            gps = {"gpsY": str(geo.latitude), "gpsX": str(geo.longitude)}

    except Exception:
        gps = {"gpsY": "null", "gpsX": "null"}

    return gps


# 현재위치
def current_location():
    try:
        here_req = requests.get("http://www.geoplugin.net/json.gp")
        if here_req.status_code != 200:
            current_gps = {"gpsY": "null", "gpsX": "null"}
        else:
            location = json.loads(here_req.text)
            current_gps = {"gpsY": str(location["geoplugin_latitude"]), "gpsX": str(location["geoplugin_longitude"])}

    except Exception:
        current_gps = {"gpsY": "null", "gpsX": "null"}

    return current_gps
