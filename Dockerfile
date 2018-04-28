FROM python:3.5.4

USER root

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y unzip wget build-essential \
            cmake git curl pkg-config libswscale-dev \
            python3-dev python3-numpy \
            libtbb2 libtbb-dev libjpeg-dev \
            libpng-dev libtiff-dev libjasper-dev \
            libboost-all-dev nodejs

RUN apt-get install -y vim
RUN apt-get install -y htop

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /code
VOLUME ["/code"]
