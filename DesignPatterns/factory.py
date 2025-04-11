from abc import ABC, abstractmethod

# ============ Implementation 1 ============

class File(ABC):

    @abstractmethod
    def edit(self):
        pass


class XmlFile(File):

    def edit(self):
        return "Editing XML file ..."


class JsonFile(File):

    def edit(self):
        return "Editing JSON file ..."


class FileFactory:

    @staticmethod
    def make_file(extension):
        if extension == "xml":
            return XmlFile()
        elif extension == "json":
            return JsonFile()


def client(extension):

    file = FileFactory.make_file(extension)
    print(file.edit())


client("json")
client("xml")


# ============ Implementation 2 ============

class Notification(ABC):
    
    @abstractmethod
    def make(self):
        pass

    def call_send(self):
        product = self.make()
        return product.send()

class SMSNotification(Notification):
    
    def make(self):
        return SMS()


class EmailNotification(Notification):
    
    def make(self):
        return Email()


class SMS:
    
    def send(self):
        return "Sending SMS notification"


class Email:
    
    def send(self):
        return "Sending Email notification"



def client(notif_type):
    
    notif_dict = {
        'sms': SMSNotification,
        'email': EmailNotification
    }
    if not notif_type in notif_dict.keys():
        raise Exception("Notification type is not valid [sms, email]")
    notification_class = notif_dict[notif_type]
    print(notification_class().call_send())

client('sms')
client('email')
