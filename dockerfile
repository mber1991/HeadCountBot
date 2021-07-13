# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

RUN useradd --create-home headcountbot
WORKDIR /home/headcountbot
USER headcountbot

COPY . .

ENV PYTHONPATH /home/headcountbot/bot/

CMD [ "python", "-m", "bot" ]