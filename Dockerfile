FROM python:3.7.0

ENV TZ=Asia/Taipei
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ARG TERM=xterm
ARG LC_ALL=C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive

COPY . /kata
WORKDIR /kata

RUN apt-get update && apt-get install -y cron

RUN apt-get install -y gconf-service libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxss1 libxtst6 libappindicator1 libnss3 libasound2 libatk1.0-0 libc6 ca-certificates fonts-liberation lsb-release xdg-utils wget git

RUN apt-get install -y fonts-cwtex-ming fonts-cwtex-kai fonts-cwtex-heib fonts-cwtex-yen fonts-cwtex-fs fonts-cwtex-docs fonts-wqy-microhei fonts-wqy-zenhei xfonts-wqy fonts-hanazono

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
