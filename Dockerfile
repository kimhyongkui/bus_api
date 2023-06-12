# base image
FROM python:3.10-slim-buster

# 환경변수 설정
ENV PYTHONUNBUFFERED=1
ENV ENVIRONMENT="dev"
ENV DB_HOST=${RDS_DB_HOST}
ENV USER_PWD=${RDS_PWD}

# 작업 디렉토리 생성 및 설정
RUN mkdir /app
WORKDIR /app

# requirements 파일 복사
COPY requirements.txt /app/

# requirements 설치
RUN pip install -r requirements.txt

# app 파일 복사
COPY . /app/

# 컨테이너 시작시 실행할 명령어
CMD [ "python", "main.py" ]


