queue = []


class MessageQueue:

    @staticmethod
    def add(response, client_type):
        queue.append((response, client_type))

    @staticmethod
    def get_first():
        response, client_type = queue[0]
        queue.pop(0)
        return response, client_type

    @staticmethod
    def get_length():
        return len(queue)
