FROM python:latest

WORKDIR /usr/src/app

ENV WIT_TOKEN=$(WIT_TOKEN)
ENV WEATHER_TOKEN=$(WEATHER_TOKEN)
ENV WOLFRAM_TOKEN=$(WOLFRAM_TOKEN)

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg -y

COPY . .
EXPOSE 50051/TCP

CMD [ "python", "./main.py" ]
