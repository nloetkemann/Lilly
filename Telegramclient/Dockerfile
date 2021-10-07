FROM python:3.7.12

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN apt-get update

COPY . .

CMD [ "python", "-u", "./main.py" ]
