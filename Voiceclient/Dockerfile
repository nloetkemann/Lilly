FROM python:latest

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install mpg123 -y

COPY . .

CMD [ "python", "./main.py" ]
