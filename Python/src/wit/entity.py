from src.message import Message
from src.wit.wit_response import WitResponse


class Entity:
    keyword = ''

    def __init__(self, wit_response, origianl_message):
        assert isinstance(wit_response, WitResponse)
        assert isinstance(origianl_message, Message)
        self.wit_response = wit_response
        self.original_message = origianl_message

    def get_response(self):
        pass
