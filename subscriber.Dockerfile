FROM python:3.9-slim-buster
WORKDIR /
ADD sub.py /
RUN pip install paho-mqtt
RUN pip install influxdb