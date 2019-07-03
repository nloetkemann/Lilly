import json
import os
from src.logic.thread import FunctionThread

history_messages = []


class History:
    name = 'history.txt'
    file = None
    histoy = []

    def __init__(self):
        if self._history_file_exists():
            self.load_history()
        else:
            self._create_history_file()

    def _create_history_file(self):
        self.file = open(self.name, 'w')
        self.file.close()

    def _history_file_exists(self):
        return os.path.exists(self.name)

    def load_history(self):
        def load(stop_thread, history_list):
            self.file = open(self.name, 'r')
            for line in self.file.readlines():
                history_list.append(json.loads(line))
            self.file.close()

        FunctionThread(load, [history_messages]).start()

    def add_to_history(self, message):
        def write_lines(stop_thread, message):
            history_messages.append(message)
            self.file = open(self.name, 'a+')

            self.file.writelines(json.dumps(message.all) + '\n')
            self.file.close()

        if message is not None:
            FunctionThread(write_lines, [message]).start()

    def delete_history(self):
        self._create_history_file()
