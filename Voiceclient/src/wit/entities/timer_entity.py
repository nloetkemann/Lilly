from src.reponse import Response
from src.wit.entity import Entity
from src.wit.objects.timer_object import TimerObject, time_object_list
import time


class TimerEntity(Entity):
    keyword = 'timer'
    time_to_sleep = 1  # in seconds

    def sleep_funtion(self, stop_thread, duration, time_object):
        assert isinstance(time_object, TimerObject)
        for i in range(duration, 0, -1):
            time.sleep(1)
            time_object.set_time(i)
            if stop_thread():
                return
        time_object.delete_from_list()
        text = 'Dein Timer ist vorbei.'
        bothandler.send_message(Response(text))

    def __get_unit(self, duration):
        if duration.find('minute') >= 0:
            return 60, 'Minute'
        elif duration.find('hour') >= 0:
            return 3600, 'Stunde'
        elif duration.find('second') >= 0:
            return 1, 'Sekunde'
        return None, None

    def _get_time_object(self):
        if self.wit_response.has_key('duration'):
            value, unit = self.wit_response.get_values('duration')
            if value is not None:
                unit_value, unit = self.__get_unit(unit)
                for time_object in time_object_list:
                    if time_object.name == str(value * unit_value) + unit:
                        return time_object
        return None

    def create_timer(self):
        if self.wit_response.has_key('duration'):
            value, unit = self.wit_response.get_values('duration')
            unit_value, unit = self.__get_unit(unit)
            if unit_value is not None:
                time_object = TimerObject(self.sleep_funtion, value * unit_value, unit)
                time_object.start_timer()
                text = 'Timer gestartet'
                return Response(text)
        else:
            return Response('Ich weiß nicht für wie lange ich den Timer stellen soll', self.original_message)

    @staticmethod
    def status_to_time(status, original_message):
        def print_seconds(seconds):
            hour = int(seconds / 3600)
            seconds -= hour * 3600
            minutes = int(seconds / 60)
            seconds -= minutes * 60
            return hour, minutes, seconds

        hour, minutes, seconds = print_seconds(status)
        hour = ' ' + str(hour) + ' Stunden' if hour > 0 else ''
        minutes = ' ' + str(minutes) + ' Minuten' if minutes > 0 else ''
        seconds = ' ' + str(seconds) + ' Sekunden' if seconds > 0 else ''
        text = 'Noch' + hour + minutes + seconds
        return Response(text, original_message)

    def status_timer(self):
        time_object = self._get_time_object()
        if time_object is not None:
            return self.status_to_time(time_object.get_status())
        else:
            if len(time_object_list) == 1:
                return self.status_to_time(time_object_list[0].get_status())
            elif len(time_object_list) > 1:
                keyboard = {}
                for time_object in time_object_list:
                    keyboard[time_object.name] = 'timer_status;' + time_object.name
                return Response('Welchen Timer meinst du?', keyboard, type='question')
            return Response('Es gibt zurzeit keine Timer.')

    def delete_timer(self):
        time_object = self._get_time_object()
        if time_object is not None:
            time_object.stop_timer()
            text = 'Dein Timer wurde gelöscht.'
            return Response(text)
        else:
            # es wurde keine Zeit angegeben, also nimmt man den ersten, wenn es nur einen Timer gibt oder man wird
            # gefragt welchen man löschen will
            if len(time_object_list) == 1:
                time_object_list[0].stop_timer()
                text = 'Dein Timer wurde gelöscht.'
                return Response(text)
            elif len(time_object_list) > 1:
                keyboard = {}
                for time_object in time_object_list:
                    keyboard[time_object.name] = 'timer_delete;' + time_object.name
                return Response('Welchen Timer willst du löschen?', keyboard, type='question')
        return Response('Es gibt keinen Timer')

    def get_response(self):
        if self.wit_response.get_values(self.keyword)[0] == 'erstelle':
            return self.create_timer()
        elif self.wit_response.get_values(self.keyword)[0] == 'status':
            return self.status_timer()
        elif self.wit_response.get_values(self.keyword)[0] == 'loesche':
            return self.delete_timer()
        else:
            return 'Ich weiß nicht was ich als Timer machen soll'
