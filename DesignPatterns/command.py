"""
This is a simple implementation of command pattern.
It can be more complex with adding undo and command history.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Command(ABC):  # Command interface

    def execute(self):
        pass


class LogCommand(Command):  # Simple command (no need to reciever)

    def __init__(self, content):
        self.content = content

    def execute(self):
        print(f"[Log] {self.content}")


class SendNotificationCommand(Command):  # Complex command

    def __init__(self, notification: "Notification", content: str):
        self.notification = notification
        self.content = content

    def execute(self):
        return self.notification.send(self.content)


class Notification(ABC):  # Reciever Interface

    @abstractmethod
    def send(self, content):
        pass


class EmailNotification(Notification):  # Concret reciever 1

    def send(self, content):
        print(f"Email sent with this content: {content}")


class SMSNotification(Notification):  # Concret reciever 2

    def send(self, content):
        print(f"SMS send with this content: {content}")


class Invoker:

    def __init__(self):
        self._commands = []

    def add_command(self, command: Command):
        self._commands.append(command)

    def remove_command(self, command: Command):
        self._commands.remove(command)

    def start(self):
        for cmd in self._commands:
            cmd.execute()


# Client
invoker = Invoker()

log_command = LogCommand(f"Sending email & sms notification at {datetime.now()}")
email_notif = SendNotificationCommand(EmailNotification(), "Hello !!!")
sms_notif = SendNotificationCommand(SMSNotification(), "Hello !!!")

invoker.add_command(log_command)
invoker.add_command(email_notif)
invoker.add_command(sms_notif)
invoker.start()
