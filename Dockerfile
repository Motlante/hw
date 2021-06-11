FROM python:3.9-slim-buster
WORKDIR /
ADD pub.py /
RUN pip install paho-mqtt