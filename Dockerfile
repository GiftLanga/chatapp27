FROM python:2.7

RUN mkdir -p /opt/services
WORKDIR /opt/services

RUN apt-get update
RUN apt-get install nano
RUN apt-get install git

RUN git clone https://github.com/GiftLanga/chatapp.git

WORKDIR /opt/services/chatapp

RUN pip install -r requirements.txt

EXPOSE 8000

CMD git pull && gunicorn --chdir chatApp --bind :8000 chatApp.wsgi:application