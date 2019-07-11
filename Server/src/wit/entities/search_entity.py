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

    def search_wiki(self):
        if not self.wit_response.has_key('query'):
            return Response('Ich weiß nicht was ich suchen soll')
        query = self.wit_response.get_values('query')[0]
        text = wikipedia.summary(query)[:300]
        array = text.split('.')
        array.pop()
        text = ''.join(array)
        return Response(text)

    def search_wolfram(self):
        if not self.wit_response.has_key('term'):
            return Response('Ich weiß nicht was ich berechnen soll')
        term = self.wit_response.get_values('term')[0]
        result = wolfram_client.query(term)
        value = next(result.results).text
        text = random_answer(self.possible_answers, 'loese').format(term, value)
        return Response(text)

    def get_response(self):
        value = self.wit_response.get_values(self.keyword)[0]
        if value == 'suche':
            return self.search_wiki()
        elif value == 'loese':
            return self.search_wolfram()
        return Response('Treffer')
