class Message:
    def __init__(self, message_text):
        self.all = message_text
        self.user = message_text['from']['first_name']
        if 'chat' in message_text:
            self.chat_id = message_text['chat']['id']
        elif 'id' in message_text:
            self.chat_id = message_text['id']
        else:
            self.chat_id = ''

        if 'text' in message_text:
            self.type = 'text'
        elif 'voice' in message_text:
            self.type = 'voice'
        elif 'document' in message_text:
            self.type = 'document'
        else:
            self.type = None

        self.is_voice_file = self.is_voice()  # could be an document type but a voice message

    def get_text(self):
        if self.is_text():
            return self.all['text']
        return None

    def get_file_id(self):
        if self.is_voice():
            return self.all['voice']['file_id']
        elif self.is_document():
            return self.all['document']['file_id']

    def is_text(self):
        return self.type == 'text'

    def is_voice(self):
        return self.type == 'voice'

    def is_document(self):
        return self.type == 'document'

    def is_command(self):
        text = self.get_text()
        if text is not None:
            return text.find('/') == 0
        return False

    # def download_file(self, path):
    #     file_id = self.get_file_id()
    #     if file_id is not None:
    #         bothandler.download_file(file_id, path)
    #     else:
    #         return None

    def get_atr(self, atribute, where=None):
        if where is None:
            if atribute in self.all:
                return self.all[atribute]
        else:
            if where in self.all:
                if atribute in self.all[where]:
                    return self.all[where][atribute]
        return None

    def set_is_voice_file(self, blub):
        self.is_voice_file = blub
