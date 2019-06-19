from random import randint

from src.reponse import Response
from src.wit.entity import Entity


class ThanksEntity(Entity):
    keyword = 'danke'
    possible_answers = {'danke': ['Für dich {}doch immer gerne', 'Es war mir eine Freude',
                                  'Ich warte dann mal auf meine nächste Aufgabe', 'Habe ich gern gemacht',
                                  'Gern geschen'],
                        'gute arbeit': ['Danke', 'Vielen dank', 'das bedeutet mir viel',
                                        'Für dich habe ich das gerne gemacht', 'Immer wieder gerne',
                                        'Das war für mich doch ein klacks', 'Ich brauche nachdem erstmal einen Kaffee',
                                        'Ach nicht der Rede wert...']}

    def get_response(self):
        value = self.wit_response.get_values(self.keyword)[0]
        if value in self.possible_answers:
            index = randint(0, len(self.possible_answers[value]) - 1)
            text = self.possible_answers[value][index]
            return Response(text, self.original_message)
        return Response('Du schmeichelst mir', self.original_message)
