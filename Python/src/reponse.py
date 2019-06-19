class Response:
    def __init__(self, text, *args,  type='message'):
        self.text = text
        self._type = type
        self.args = args

    def get_type(self):
        return self._type

    def is_question(self):
        return self._type == 'question'

    def is_message(self):
        return self._type == 'message'
