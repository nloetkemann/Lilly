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

    def contains_custom_keyboard(self):
        return self._type == 'message' and isinstance(self.args, list)

    def get_args(self):
        if self.is_question() or self.contains_custom_keyboard():
            return self.args[0]
