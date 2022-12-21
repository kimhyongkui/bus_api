from PIL import Image
import requests
import io
from dotenv import load_dotenv
import os
from api_vehicle import gpsxy


load_dotenv()
client_id = os.getenv('NAVER_ID')
client_secret = os.getenv('naver_key')


# 좌표 (경도, 위도)
endpoint = "https://naveropenapi.apigw.ntruss.com/map-static/v2/raster"
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
}


gpsxy_dict = gpsxy()



def getmap():
    i = 0
    for gpsxy in gpsxy_dict:
        i += 1
        # 중심 좌표
        lon, lat = gpsxy['gpsX'], gpsxy['gpsY']
        center = f"{lon},{lat}"
        # 줌 레벨 - 0 ~ 20
        level = 14
        # 가로 세로 크기 (픽셀)
        w, h = 800, 800
        # 지도 유형 - basic, traffic, satellite, satellite_base, terrain
        maptype = "satellite"
        # 반환 이미지 형식 - jpg, jpeg, png8, png
        format = "png"
        # 고해상도 디스펠레이 지원을 위한 옵션 - 1, 2
        scale = 1
        # 마커
        markers = f"""type:d|size:mid|pos:{lon} {lat}|color:red"""
        # 라벨 언어 설정 - ko, en, ja, zh
        lang = "ko"
        # 대중교통 정보 노출 - Boolean
        public_transit = True
        # 서비스에서 사용할 데이터 버전 파라미터 전달 CDN 캐시 무효화
        dataversion = ""

        # URL
        url = f"{endpoint}?center={center}&level={level}&w={w}&h={h}&maptype={maptype}&format={format}&scale={scale}&markers={markers}&lang={lang}&public_transit={public_transit}&dataversion={dataversion}"
        res = requests.get(url, headers=headers)
        image_data = io.BytesIO(res.content)
        image = Image.open(image_data)
        image.save(f"""C:/Users/abc/Desktop/코딩/{i}.png""", 'png')

    print("출력끝")

getmap()

