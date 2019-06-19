from src.reponse import Response
from src.wit.entity import Entity


class MessageEntity(Entity):
    keyword = 'message'

    def get_name_from_message(self):
        if self.wit_response.has_key('name'):
            return self.wit_response.get_values('name')[0]
        else:
            return None

    def get_message_from_message(self):
        return self.wit_response.get_values('message')[0]

    def get_response(self):
        name = self.get_name_from_message()
        if name is None:
            text = 'Ich weiß leider nicht für wen die Nachricht ist...'
            return Response(text, self.original_message)
        text = name + ', ich soll dir das von ' + self.original_message.user + ' sagen:\n' + \
               self.get_message_from_message()
        return Response(text, self.original_message)
