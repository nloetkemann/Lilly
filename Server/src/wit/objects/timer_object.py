from src.logic.thread import FunctionThread
from src.wit.objects.abstract_object import AbstractObject


class TimerObject(AbstractObject):

    def __init__(self, function, *args):
        super().__init__(function)
        self.thread = FunctionThread(function, args=[args[0], self])
        self.name = str(args[0]) + ' ' + args[1]
        self.value = args[0]
        self.unit = args[1]
        time_object_list.append(self)

    def stop_timer(self):
        self.thread.stop()
        self.delete_from_list()

    def delete_from_list(self):
        time_object_list.remove(self)


time_object_list = []
