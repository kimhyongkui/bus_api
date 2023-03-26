import requests
import json
from geopy.geocoders import Nominatim
from fastapi import status, HTTPException


# 지오코딩 : 지역이름을 적으면 좌표가 나온다
def specific_location(address):
    try:
        location = Nominatim(user_agent='South Korea')
        geo = location.geocode(address)

        if geo is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")

        else:
            gps = {"gpsY": str(geo.latitude), "gpsX": str(geo.longitude)}

        return gps

    except HTTPException:
        raise

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


# 현재위치
def current_location():
    try:
        here_req = requests.get("http://www.geoplugin.net/json.gp")

        if here_req.status_code != 200:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="잘못된 매개변수 입력")

        else:
            location = json.loads(here_req.text)
            current_gps = {"gpsY": str(location["geoplugin_latitude"]), "gpsX": str(location["geoplugin_longitude"])}

        return current_gps

    except HTTPException:
        raise

    except TimeoutError:
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="geoplugin 접속 오류")

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
