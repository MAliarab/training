# ============ Implementation 1 ============

from abc import ABC, abstractmethod


class OldPaymentService:

    def make_payment(self):
        return "Old payment process"


class NewPaymentInterface(ABC):

    @abstractmethod
    def new_payment_process(self):
        pass


class PaymentAdapter(NewPaymentInterface):

    def __init__(self, old_payment_service: OldPaymentService):
        self.old_payment_service = old_payment_service

    def new_payment_process(self):
        return f"Adapted: {self.old_payment_service.make_payment()}"


def client(new_payment: NewPaymentInterface):
    print(new_payment.new_payment_process())
    print("-" * 20)


client(PaymentAdapter(OldPaymentService()))


# ============ Implementation 2 ============


import xmltodict


# this class works with xml
class Application:

    def send_request(self):
        return "./DesignPatterns/data/employees.xml"


# this class works with dictionary (json)
class Analytics:

    def data_analyzer(self, dic):
        return f"This is the result on {dic}"


class DataAdapter(ABC):

    @abstractmethod
    def get_data(self):
        pass


class XmlToJSONAdapter(DataAdapter):

    def __init__(self, application: Application):
        self.application = application

    def get_data(self):
        xml_path = self.application.send_request()
        with open(xml_path, "r") as file:
            obj = xmltodict.parse(file.read())
        return obj


def client(adapter: DataAdapter, analytics: Analytics):
    obj = adapter.get_data()
    result = analytics.data_analyzer(obj)
    print(result)
    print("-" * 20)


client(XmlToJSONAdapter(Application()), Analytics())
