import os
from src.logic.tools import random_answer
from src.logic.reponse import Response
from src.wit.entity import Entity
import wikipedia
import wolframalpha

wolfram_key = os.environ['WOLFRAM_TOKEN']
wolfram_client = wolframalpha.Client(wolfram_key)
wikipedia.set_lang('de')


class SearchEntity(Entity):
    keyword = 'suche'
    possible_answers = {'suche': [],
                        'loese': ['Das Ergebnis von {} ist {}', '{} ist {}']}

    class Wolfram:
        possible_answers = ['Das Ergebnis von {} ist {}', '{} ist {}']

        def search(self, wit_response):
            if not wit_response.has_key('term'):
                return Response('Ich weiß nicht was ich berechnen soll')
            term = wit_response.get_values('term')[0]
            result = wolfram_client.query(term)
            value = next(result.results).text
            text = random_answer(self.possible_answers).format(term, value)
            return Response(text)

    class Wikipedia:

        def search(self, wit_response):
            if not wit_response.has_key('query'):
                return Response('Ich weiß nicht was ich suchen soll')
            query = wit_response.get_values('query')[0]
            try:
                text = wikipedia.summary(query)[:300]
                array = text.split('.')
                array.pop()
                text = ''.join(array)
                return Response(text)
            except wikipedia.exceptions.DisambiguationError as e:
                if e.options and isinstance(e.options, list):
                    return Response("Was genau suchst du?", e.options, 'seach_wiki', type="question")

    def get_response(self):
        value = self.wit_response.get_values(self.keyword)[0]
        if value == 'suche':
            return self.Wikipedia().search(self.wit_response)
        elif value == 'loese':
            return self.Wolfram().search(self.wit_response)
        return Response('Treffer')
