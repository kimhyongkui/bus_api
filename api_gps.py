import requests, json
from geopy.geocoders import Nominatim
from api_station import get_stn_list

# 현재위치
def current_location():
    here_req = requests.get("http://www.geoplugin.net/json.gp")

    if (here_req.status_code != 200):
        print("현재좌표를 불러올 수 없음")
    else:
        location = json.loads(here_req.text)
        current_gps = {"gpsY": str(location["geoplugin_latitude"]), "gpsX": str(location["geoplugin_longitude"])}
        # print(gps['gpsY'], gps['gpsX'])
    return current_gps



# 지오코딩 : 지역이름 적으면 좌표나오는거
def geocoding(address):
    geolocoder = Nominatim(user_agent='South Korea')
    geo = geolocoder.geocode(address)
    gps = {"gpsY": str(geo.latitude), "gpsX": str(geo.longitude)}

    return gps


# 특정 지역 좌표 입력해서 인근 정류소 구해보기
def get_station_list(address, rad):
    adr = geocoding(address)
    gps = get_stn_list(adr['gpsX'], adr['gpsY'], rad)
    data_list = []
    for data in range(len(gps)):
        data_dict = {}
        data_dict['stnId'] = gps[data]['stnId']
        data_dict['stnNm'] = gps[data]['stnNm']
        data_dict['arsId'] = gps[data]['arsId']
        data_dict['dist'] = gps[data]['dist']
        data_list.append(data_dict)

    return data_list



