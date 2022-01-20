FROM ubuntu:latest

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get install -y nginx 

COPY requirements.txt /requirements.txt

COPY nginx.conf /etc/nginx/sites-available/nginx.conf
COPY uwsgi_params /etc/nginx/uwsgi_params
RUN ln -s /etc/nginx/sites-available/nginx.conf /etc/nginx/sites-enabled


RUN apt-get install -y  apt-utils python3-dev python3-setuptools python3-pip \
                        gcc libc-dev \
                        libffi-dev libssl-dev musl-dev && \
    pip install --upgrade pip && \
    pip install -r /requirements.txt  


CMD ["bin/bash"]