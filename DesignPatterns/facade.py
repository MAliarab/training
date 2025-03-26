# Subsystems
class Authentication:

    def authenticate(self):
        return "User autheticated"


class Payment:

    def payment_process(self):
        return "Payment process done"


class Notification:

    def send_notification(self):
        return "Notification sent"


# Facade
class PaymentFacade:

    def __init__(
        self,
        authetication: Authentication,
        payment: Payment,
        notification: Notification,
    ):
        self._authentication = authetication
        self._payment = payment
        self._notification = notification

    def make_payment(self):
        authentication_result = self._authentication.authenticate()
        payment_result = self._payment.payment_process()
        notification_result = self._notification.send_notification()
        return f"{authentication_result}\n{payment_result}\n{notification_result}"


def client():
    payment_facade = PaymentFacade(Authentication(), Payment(), Notification())
    print(payment_facade.make_payment())


client()
