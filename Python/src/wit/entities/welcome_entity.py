from src.reponse import Response
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

    def get_name(self):
        random = randint(0, 2)
        if random == 1:
            return self.original_message.user
        return ''

    def get_response(self):
        value = self.wit_response.get_values(self.keyword)[0]
        if value in self.possible_answers:
            index = randint(0, len(self.possible_answers[value]) - 1)
            text = self.possible_answers[value][index] + ' ' + self.get_name()
            return Response(text, self.original_message)
        return Response('Hi ' + self.get_name(), self.original_message)
