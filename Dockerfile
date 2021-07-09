FROM python:3.9-slim-buster

RUN apt update && apt install -y git && apt-get clean
RUN python -m pip install Django
RUN python -m pip install -U autopep8 --user

COPY . $APP_HOME
