from abc import ABC, abstractmethod
from typing import List
from enum import Enum


class EventType(Enum):
    PAYMENT_DONE = "Payment Done"
    PUBLISH_BILL = "Publish Bill"
    REFUND_ORDER = "Refund Order"
    SMS_SENT = "SMS Sent"


class Mediator(ABC):  # Abstract Mediator

    @abstractmethod
    def notify(self, sender, event):
        pass


class ServiceCommunication(Mediator):  # Concrete Mediator

    def __init__(
        self, sender_service: "BaseService", receiver_services: List["BaseService"]
    ):
        self.sender_service = sender_service
        self.sender_service.set_mediator(self)

        self.receiver_services = receiver_services
        for service in self.receiver_services:
            service.set_mediator(self)

    def notify(self, sender: "BaseService", event: EventType):
        for service in self.receiver_services:
            service.receive(sender, event)


class BaseService(ABC):  # Abstract Component

    def __init__(self):
        self._mediator = None

    def set_mediator(self, mediator: Mediator):
        self._mediator = mediator

    @abstractmethod
    def receive(self, sender: "BaseService", event: EventType):
        pass

    @abstractmethod
    def notify(self, event):
        pass


class PaymentService(BaseService):  # Concrete Component 1

    def receive(self, sender, event):
        print(
            f"Payment service received event ({event}) from sender ({sender.__class__.__name__})"
        )

    def notify(self, event):
        self._mediator.notify(self, event)

    def payment_process(self):
        print("Payment process done!")
        self.notify(EventType.PAYMENT_DONE.value)


class BillService(BaseService):  # Concrete Component 2

    def receive(self, sender, event):
        print(
            f"Bill service received event ({event}) from sender ({sender.__class__.__name__})"
        )

    def notify(self, event):
        self._mediator.notify(self, event)

    def publish_bill(self):
        print("Bill published!")
        self.notify(EventType.PUBLISH_BILL.value)

    def refund(self):
        print("Order refunded!")
        self.notify(EventType.REFUND_ORDER.value)


class SMSNotificationService(BaseService):  # Concrete Component 3

    def receive(self, sender, event):
        print(
            f"SMS service received event ({event}) from sender ({sender.__class__.__name__})"
        )

    def notify(self, event):
        self._mediator.notify(self, event)

    def send_sms(self):
        print("sms sent!")
        self.notify(EventType.SMS_SENT.value)


# client

# Payment Done process
print("-------- Scenario 1 --------")
payment_service = PaymentService()
bill_service = BillService()
sms_notif_service = SMSNotificationService()

payment_service_communication = ServiceCommunication(
    payment_service, [bill_service, sms_notif_service]
)
payment_service.payment_process()


# Refund Process
print("-------- Scenario 2 --------")
refund_communication = ServiceCommunication(
    bill_service, [payment_service, sms_notif_service]
)
bill_service.refund()
