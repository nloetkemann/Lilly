from src.wit.wit_response import WitResponse


class Entity:
    keyword = ''

    def __init__(self, wit_response):
        assert isinstance(wit_response, WitResponse)
        self.wit_response = wit_response

    def get_response(self):
        pass
