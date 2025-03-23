from abc import ABC, abstractmethod


class EmailNotification(ABC):

    @abstractmethod
    def send_email(self):
        pass


class SMSNotification(ABC):

    @abstractmethod
    def send_sms(self):
        pass


class ShortSMSNotification(SMSNotification):

    def send_sms(self):
        return "Sending [short] sms notification ..."


class LongSMSNotification(SMSNotification):

    def send_sms(self):
        return "Sending [long] sms notification ..."


class ShortEmailNotification(EmailNotification):

    def send_email(self):
        return "Sending [short] email notification ..."


class LongEmailNotification(EmailNotification):

    def send_email(self):
        return "Sending [long] email notification ..."


class NotificationFactory(ABC):

    @staticmethod
    @abstractmethod
    def make_email_notification():
        pass

    @staticmethod
    @abstractmethod
    def make_sms_notification():
        pass


class ShortNotificationFactory(NotificationFactory):

    @staticmethod
    def make_email_notification():
        return ShortEmailNotification()

    @staticmethod
    def make_sms_notification():
        return ShortSMSNotification()


class LongNotificationFactory(NotificationFactory):

    @staticmethod
    def make_email_notification():
        return LongEmailNotification()

    @staticmethod
    def make_sms_notification():
        return LongSMSNotification()


def client(notification: NotificationFactory):
    email_notifier = notification.make_email_notification()
    sms_notifier = notification.make_sms_notification()

    print(email_notifier.send_email())
    print(sms_notifier.send_sms())


client(LongNotificationFactory)
client(ShortNotificationFactory)
