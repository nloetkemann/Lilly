FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir temp

RUN apt-get update
RUN apt-get install ffmpeg -y

COPY . .
EXPOSE 50051/TCP

CMD [ "python3", "-u", "./main.py" ]
