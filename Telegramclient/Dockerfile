FROM python:latest

WORKDIR /usr/src/app

RUN mkdir temp

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update

COPY . .

CMD [ "python", "-u", "./main.py" ]
