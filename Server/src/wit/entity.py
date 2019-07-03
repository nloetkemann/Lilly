from src.wit.wit_response import WitResponse


class Entity:
    keyword = ''

    def __init__(self, wit_response):
        assert isinstance(wit_response, WitResponse)
        # assert isinstance(origianl_message, Message)
        self.wit_response = wit_response
        # self.original_message = origianl_message

    def _welcome(self, welcome_entity):
        key = 'begruessung'
        if self.wit_response.has_key(key):
            value = self.wit_response.get_values(key)[0]
            return welcome_entity.get_greeting(welcome_entity.possible_answers, value)

    def get_response(self):
        pass
