from src.message import Message
from src.reponse import Response
from src.wit.entity import Entity
from pytz import timezone
from src.wit.wit_response import WitResponse
import requests
import os
from datetime import datetime

weather_key = os.environ['WEATHER_TOKEN']


class IntentEntity(Entity):
    keyword = 'intent'

    class WeatherEntity:
        location = 'Espelkamp'
        date = ''
        url = 'https://api.openweathermap.org/data/2.5/forecast?q={},de&units=metric&lang=de&appid=' + weather_key

        def __init__(self, wit_response, message):
            assert isinstance(wit_response, WitResponse)
            self.wit_response = wit_response
            self.original_message = message

        def check_location_in_message(self):
            if self.wit_response.has_key('location'):
                self.location = self.wit_response.get_values('location')[0]
                return True
            return False

        def check_date_in_message(self):
            if self.wit_response.has_key('datetime'):
                self.date = int(datetime.fromisoformat(self.wit_response.get_values('datetime')[0]).timestamp())
                return True
            return False

        def _do_request(self, url):
            r = requests.get(url)
            if r.status_code != 200:
                return 'Ich konnte das Wetter leider nicht abfragen...'
            return r.json()

        def weather_today(self, response):
            today = response['list'][0]
            temperature = today['main']['temp']
            description = today['weather'][0]['description']
            return temperature, description

        def weather_forecast(self, response):

            def compare_tmstp(target, tmstp):
                if target - tmstp < max_diff:
                    return tmstp

            max_diff = 10800
            weather_list = response['list']

            for weather in weather_list:
                if compare_tmstp(self.date, weather['dt']) is not None:
                    return weather['main']['temp'], weather['weather'][0]['description']

            return None, None

        def get_weather(self):
            set_location = self.check_location_in_message()
            url = self.url.format(self.location)
            set_date = self.check_date_in_message()

            response = self._do_request(url)
            if set_date:
                temperature, description = self.weather_forecast(response)
            else:
                temperature, description = self.weather_today(response)

            if temperature is None or description is None:
                return Response('Ich konnte das Wetter nicht laden...', self.original_message)

            if set_location:
                if set_date:
                    text = 'Es wird ' + str(int(temperature)) + ' Grad in ' + self.location + 'mit ' + description
                    return Response(text, self.original_message)
                text = 'In ' + self.location + ' ist es ' + str(int(temperature)) + ' Grad mit ' + description
                return Response(text, self.original_message)
            else:
                if set_date:
                    text = 'Es wird ' + str(int(temperature)) + ' Grad mit ' + description
                    return Response(text, self.original_message)
                text = 'Es ist ' + str(int(temperature)) + ' Grad mit ' + description
                return Response(text, self.original_message)

    class TimeEntity:

        def __init__(self, message):
            assert isinstance(message, Message)
            self.message = message

        def get_time(self):
            time = datetime.now(timezone('Europe/Berlin')).time().strftime('%H:%M')
            return Response('Es ist ' + time, self.message)

    def get_value(self):
        if self.wit_response.get_values(self.keyword)[0] == 'uhr':
            return self.TimeEntity(self.original_message).get_time()
        elif self.wit_response.get_values(self.keyword)[0] == 'wetter':
            return self.WeatherEntity(self.wit_response, self.original_message).get_weather()

    def get_response(self):
        return self.get_value()
