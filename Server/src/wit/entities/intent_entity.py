from random import randint

from src.logic.reponse import Response
from src.logic.tools import random_answer
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
        weather_comments = {
            'regen': ['Der Regen ist nur ziemlich nervig', 'Ich habe nur genug von dem Wetter',
                      'Ich bin nur nicht so der Regen Fan'],
            'bedeckt': ['Mir fehlt die Sonne', 'Ein bisschen Sonne wäre aber ganz gut', 'Ich warte auf die Sonne...']
        }
        possible_answers = {'no_location': ['Es ist {weather} mit {temperature} Grad',
                                            'Draußen ist es {weather} mit {temperature} Grad'],
                            'no_location_future': ['Es wird {weather} sein, mit {temperature} Grad'],
                            'location': ['In {location} ist es {weather} mit {temperature} Grad',
                                         ],
                            'location_future': ['In {location} wird es {weather} sein, mit {temperature} Grad',
                                                ]
                            }

        def __init__(self, wit_response):
            assert isinstance(wit_response, WitResponse)
            self.wit_response = wit_response

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

        # complete method for using weather in other entities
        @staticmethod
        def only_get_weather_today():
            location = IntentEntity.WeatherEntity.location
            url = IntentEntity.WeatherEntity.url.format(location)
            response = IntentEntity.WeatherEntity.do_request(url)
            return IntentEntity.WeatherEntity.weather_today(response)

        @staticmethod
        def do_request(url):
            r = requests.get(url)
            if r.status_code != 200:
                return 'Ich konnte das Wetter leider nicht abfragen...'
            return r.json()

        @staticmethod
        def weather_today(response):
            today = response['list'][0]
            temperature = today['main']['temp']
            description = today['weather'][0]['description']
            return temperature, description

        @staticmethod
        def weather_forecast(response, date):

            def compare_tmstp(target, tmstp):
                if target - tmstp < max_diff:
                    return tmstp

            max_diff = 10800
            weather_list = response['list']

            for weather in weather_list:
                if compare_tmstp(date, weather['dt']) is not None:
                    return weather['main']['temp'], weather['weather'][0]['description']

            return None, None

        def get_weather(self):
            set_location = self.check_location_in_message()
            url = self.url.format(self.location)
            set_date = self.check_date_in_message()

            response = self.do_request(url)
            if set_date:
                temperature, description = self.weather_forecast(response, self.date)
            else:
                temperature, description = self.weather_today(response)

            if temperature is None or description is None:
                return Response('Ich konnte das Wetter nicht laden...')

            description = description.lower()
            temperature = str(int(temperature))

            if set_location:
                if set_date:
                    return Response(random_answer(self.possible_answers, 'location_future').format(
                        location=self.location,
                        weather=description,
                        temperature=temperature))
                return Response(random_answer(self.possible_answers, 'location').format(
                    location=self.location,
                    weather=description,
                    temperature=temperature))
            else:
                if set_date:
                    return Response(random_answer(self.possible_answers, 'no_location_future').format(
                        weather=description,
                        temperature=temperature))
                return Response(random_answer(self.possible_answers, 'no_location').format(
                    weather=description,
                    temperature=temperature))

    class TimeEntity:

        def get_time(self):
            time = datetime.now(timezone('Europe/Berlin')).time().strftime('%H:%M')
            return Response('Es ist ' + time)

    class NameEntity:
        name = 'Lilly'
        possible_answers = [f'Mein Name ist {name}', f'Die meisten Leute nennen mich {name}',
                            f'Du kannst mich {name} nennen', f'{name}, einfach nur {name}']

        def get_name(self):
            index = randint(0, len(self.possible_answers) - 1)
            text = self.possible_answers[index]
            return Response(text)

    class DateEntity:
        possible_answers = ['Heute ist {day} der {daynumber} {month}', 'Es ist {day}, der {daynumber}. {month}']

        def __init__(self, wit_response):
            assert isinstance(wit_response, WitResponse)
            self.wit_response = wit_response

        def _get_specific_date(self):
            if self.wit_response.has_key('date'):
                return datetime.fromisoformat(self.wit_response.get_values('date')[0])
            return None

        @staticmethod
        def _get_week_day_by_number(day_number):
            if day_number in range(0, 7):
                weeklist = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
                return weeklist[day_number]

        @staticmethod
        def _get_month_name_by_number(month):
            if month in range(0, 12):
                monthlist = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli',
                             'August', 'September', 'Oktober', 'November', 'Dezember']
                return monthlist[month]

        def get_date(self):
            date = self._get_specific_date()
            if date is None:
                date = datetime.now(timezone('Europe/Berlin'))
            weekday = self._get_week_day_by_number(date.weekday())
            day = date.day
            month = self._get_month_name_by_number(date.month)
            text = random_answer(self.possible_answers).format(day=day, daynumber=weekday, month=month)
            return Response(text)

    def get_value(self):
        if self.wit_response.get_values(self.keyword)[0] == 'uhr':
            return self.TimeEntity().get_time()
        elif self.wit_response.get_values(self.keyword)[0] == 'wetter':
            return self.WeatherEntity(self.wit_response).get_weather()
        elif self.wit_response.get_values(self.keyword)[0] == 'datum':
            return self.DateEntity(self.wit_response).get_date()
        elif self.wit_response.get_values(self.keyword)[0] == 'name':
            return self.NameEntity().get_name()

    def get_response(self):
        return self.get_value()
