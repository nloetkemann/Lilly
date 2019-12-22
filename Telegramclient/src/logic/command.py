from src.logic.bot_handler import bothandler
from src.logic.message import Message
from src.logic.reponse import Response

file_mode = 'command'


class CommandHandler:

    def __init__(self, message):
        assert isinstance(message, Message)
        self.message = message

    @staticmethod
    def get_file_mode():
        global file_mode
        return file_mode

    @staticmethod
    def set_file_mode(mode):
        global file_mode
        file_mode = mode

    def file_mode(self):
        bothandler.send_question(
            Response('Was soll ich mit den Audiodateien machen?',
                     self.message,
                     {'Übersetzen': "change_mode;translate", 'Befehl': "change_mode;command"},
                     type='question'))

    def help(self):
        bothandler.send_message(Response('Hier ist deine Hilfe...', self.message))

    def get_command(self, command):
        command = command.replace("/", "")
        if command == 'help':
            return self.help()
        elif command == 'voice_mode':
            return self.file_mode()

    class Callback:
        chat_id = ""

        # Hier wird die Methode ausgeführt, die als Callback zurück kam
        def callback_action(self, data, chat_id):
            self.chat_id = chat_id
            split = data.split(';')
            if len(split) == 1:
                method = split[0]
                return getattr(self, method)()
            else:
                method, args = split
                return getattr(self, method)(args)

        def seach_wiki(self, args):
            from src.grpc.client import client   # import later because of a circular dependency
            #  todo reguest an server direkt an die Wiki entitaet
            client.single_message('wer ist ' + args, self.chat_id)

        def show_help(self):
            return """
    Hier ist deine Hilfe:
    Du kannst mehrere Abfragen machen, z.B. das Wetter abfragen:
    Wie ist das Wetter
    Wie viel Uhr ist es

    Hier sind ein paar andere Möglichkeiten
    Timer stellen:
    stelle einen Timer für 2 minuten
    wie weit ist der 2 minuten Timer
    lösche den 2 minuten Timer

    Erinnerung erstellen:
    'erinnere mich um 2 uhr daran Wäsche zu waschen'
    'lösche die Erinnerung um 2 Uhr'
            """

        def show_usage(self):
            return 'Hier ist dein Gebrauch'

        def change_mode(self, mode):
            CommandHandler.set_file_mode(mode)
