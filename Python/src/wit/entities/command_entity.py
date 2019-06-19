from src.reponse import Response
from src.wit.entity import Entity

voice_mode = 't'  # t=translate(get Content of voice message), m=normal Message(using voice Message as normal Message)


class CommandEntity(Entity):
    keyword = 'command'
    voice_mode = 't'

    @staticmethod
    def set_voice_mode(self, mode):
        self.voice_mode = mode

    @staticmethod
    def get_voice_mode(self):
        return self.voice_mode

    class HelpEntity:

        def get_help(self):
            return Response('Welche Hilfe möchtest du haben?',
                            {'Hilfe': 'show_help', 'Usage': 'show_usage'}, type='question')

    class VoiceModeEntity:

        def question_change_mode(self):
            return Response('Wie sollen Sprachnachrichten behandelt werden?',
                            {'als Befehl': 'change_mode;m',
                             'als Text asugeben': 'change_mode;t'},
                            type='question')

    def get_response(self):
        if self.wit_response.get_values(self.keyword)[0] == 'help':
            return self.HelpEntity().get_help()
        elif self.wit_response.get_values(self.keyword)[0] == 'voice_mode':
            return self.VoiceModeEntity().question_change_mode()
        else:
            return Response('Ich habe nicht den passenden Befehl gefunden')
