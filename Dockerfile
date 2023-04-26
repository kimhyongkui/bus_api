# base image
FROM python:3.10-slim-buster

# set environment variable
ENV PYTHONUNBUFFERED=1

# create and set working directory
RUN mkdir /app
WORKDIR /app

# copy requirements file
COPY requirements.txt /app/

# install requirements
RUN pip install -r requirements.txt

# copy app files
COPY . /app/

# command to run on container start
CMD [ "python", "main.py" ]


