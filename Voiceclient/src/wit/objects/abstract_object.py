class AbstractObject:
    counter = 0
    thread = None  # is
    name = ''

    def __init__(self, function):
        pass

    def start_timer(self):
        self.thread.start()

    def stop_timer(self):
        self.thread.stop()
        self.__del__()

    def get_status(self):
        return self.counter

    def set_time(self, counter):
        self.counter = counter

    def __del__(self):
        pass
