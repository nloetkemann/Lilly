from datetime import datetime

from src.logic.message_queue import MessageQueue
from src.logic.reponse import Response
from src.wit.entity import Entity
from src.wit.objects.notification_object import NotificationObject, notification_object_list
from pytz import timezone
import time


class NotificationEntity(Entity):
    keyword = 'erinnerung'

    def sleep_funtion(self, stop_thread, duration, text_message, notification_object):
        assert isinstance(notification_object, NotificationObject)
        for i in range(duration, 0, -1):
            time.sleep(1)
            notification_object.set_time(i)
            if stop_thread():
                notification_object.stop_timer()
                return
        notification_object.delete_from_list()
        text = 'Ich soll dich daran erinnern \n"' + text_message + '"'
        MessageQueue.add(Response(text), self.client_type)

    def _get_message(self):
        if self.wit_response.has_key('message_erinnerung'):
            return self.wit_response.get_values('message_erinnerung')[0]

    def __get_unit(self, duration):
        if duration.find('minute') >= 0:
            return 60, 'Minute'
        elif duration.find('stunde') >= 0:
            return 3600, 'Stunde'
        elif duration.find('second') >= 0:
            return 1, 'Sekunde'

    def _get_time(self):
        current_timestamp = int(datetime.now(timezone('Europe/Berlin')).timestamp())
        if self.wit_response.has_key('datetime'):
            future_timestampt = int(datetime.fromisoformat(self.wit_response.get_values('datetime')[0]).timestamp())
            return future_timestampt - current_timestamp, future_timestampt
        elif self.wit_response.has_key('duration'):
            value, unit = self.wit_response.get_values('duration')
            if value is not None:
                unit_value, unit = self.__get_unit(unit)
                if unit_value is not None:
                    return value * unit_value, current_timestamp + value * unit_value

    def notification_status(self):
        length = len(notification_object_list)
        if length == 0:
            return 'Du hast noch keine Benachrichtigungen.'
        elif length == 1:
            response = 'Du hast eine Benachrichtigung.\n'
        else:
            response = 'Du hast ' + str(length) + ' Benachrichtigungen.\n'
        for notification in notification_object_list:
            dt = datetime.fromtimestamp(notification.finish_time, timezone('Europe/Berlin')).strftime(
                '%Y.%m.%d %H:%M:%S')
            current_date = datetime.now(timezone('Europe/Berlin')).strftime('%Y.%m.%d')
            date, finished_time = dt.split(' ')
            if date == current_date:
                response += 'Um ' + str(finished_time)
            else:
                response += 'Am ' + date + ' um ' + finished_time
            response += ' die Erinnerung "' + notification.message + '"\n'
        return response

    def delete_notification(self):
        time_value, finish_time = self._get_time()
        if finish_time is None:
            text = 'Ich weiß nicht welchen Timer ich löschen soll'
            return Response(text)
        for notification_object in notification_object_list:
            if notification_object.finish_time == int(finish_time):
                notification_object.stop_timer()
                text = 'Deine Erinnerung wurde gelöscht.'
                return Response(text)

    def create_notification(self):
        message = self._get_message()
        if message is None:
            return Response('Mir fehlt die Nachricht')
        time_value, finish_time = self._get_time()
        if time_value is None:
            text = 'Ich weiß nicht zu wann ich die Erinnerung stellen soll'
            return Response(text)

        NotificationObject(self.sleep_funtion, time_value, message, finish_time).start_timer()
        return Response('Erinnerung erstellt.')

    def get_notifications(self):
        return Response('status')

    def get_response(self):
        if self.wit_response.get_values(self.keyword)[0] == 'benachrichtige mich':
            return self.create_notification()
        elif self.wit_response.get_values(self.keyword)[0] == 'loesche benachrichtigung':
            return self.delete_notification()
        elif self.wit_response.get_values(self.keyword)[0] == 'status benachrichtigung':
            return self.notification_status()
        else:
            return 'Ich bin mir nicht sicher was ich mit der Benachrichtigung machen soll.'
