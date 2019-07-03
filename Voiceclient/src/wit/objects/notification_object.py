from src.logic.thread import FunctionThread
from src.wit.objects.abstract_object import AbstractObject


class NotificationObject(AbstractObject):
    def __init__(self, function, *args):
        super().__init__(function)
        self.thread = FunctionThread(function, args=[args[0], args[1], self])
        self.name = str(args[0]) + 'Erinnerung'
        notification_object_list.append(self)
        self.finish_time = int(args[2])
        self.message = args[1]

    def stop_timer(self):
        self.thread.stop()
        self.delete_from_list()

    def delete_from_list(self):
        notification_object_list.remove(self)


notification_object_list = []
