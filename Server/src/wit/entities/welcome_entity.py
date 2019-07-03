from src.logic.tools import random_answer
from src.logic.reponse import Response
from src.wit.entities.intent_entity import IntentEntity
from src.wit.entity import Entity
from random import randint


class WelcomeEntity(Entity):
    keyword = 'begruessung'
    possible_answers = {'hallo': ['Moin Moin', 'Hi', 'Hallöchen', 'Moin',
                                  'Einen wunderschönen guten Morgen', 'Guten Morgen'],
                        'wie geht es': ['danke sehr gut', 'ich kann mich nicht beklagen',
                                        'ich bin etwas müde von meiner Nachtschicht',
                                        'Mir geht es heute sehr gut.'],
                        'guten morgen': ['dir auch einen guten morgen', 'Moin Moin',
                                         'den habe ich erst nach dem ersten Kaffee']}

    @staticmethod
    def check_weather(key):
        if key != 'wie geht es':
            return ''
        answers = IntentEntity.WeatherEntity.weather_comments
        temp, desc = IntentEntity.WeatherEntity.only_get_weather_today()
        if desc.lower().find('regen') >= 0:
            return '\n' + random_answer(answers, 'regen')
        elif desc.lower().find('bedeckt') >= 0:
            return '\n' + random_answer(answers, 'bedeckt')
        return ''

    # def get_name(self):
    #     random = randint(0, 2)
    #     if random == 1:
    #         return self.original_message.user
    #     return ''

    @staticmethod
    def get_greeting(possible_answers, key):
        if key in possible_answers:
            greeting = random_answer(possible_answers, key)
            return greeting
        return ''

    def get_response(self):
        values = self.wit_response.get_values(self.keyword)
        text = ''
        if len(values) > 1:
            if values[1] == 'wie geht es':
                text += WelcomeEntity.get_greeting(self.possible_answers, values[0])
                text += '\n' + WelcomeEntity.get_greeting(self.possible_answers, values[1])
                text += WelcomeEntity.check_weather(values[1])
        else:
            text += WelcomeEntity.get_greeting(self.possible_answers, values[0])
            # text += ' ' + self.get_name()
            text += WelcomeEntity.check_weather(values[0])
        if text != '':
            return Response(text)
        return Response('Hi')
