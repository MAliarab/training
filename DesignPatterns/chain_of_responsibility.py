from abc import ABC, abstractmethod
from datetime import datetime


class AbstractHandler(ABC):

    @abstractmethod
    def set_next(self, handler: "AbstractHandler") -> "AbstractHandler":
        pass

    @abstractmethod
    def handle(self, request: dict):
        pass


class BaseHandler(AbstractHandler):

    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: dict):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class AuthenticationHandler(BaseHandler):

    def handle(self, request):
        if not request.get("authenticated", False):
            return "401 not authenticated !!!"
        return super().handle(request)


class AuthorizationHandler(BaseHandler):

    def handle(self, request):
        if request.get("role") != "admin":
            return "403 forbidden !!!"
        return super().handle(request)


class LogHandler(BaseHandler):

    def handle(self, request):
        print(f"[Log] Request {request} recieved at: {datetime.now()}")
        return super().handle(request)


class DefaultHandler(BaseHandler):

    def handle(self, request):
        return f"Request {request} proceed successful"


def client(handler: AbstractHandler, request: dict):
    print(handler.handle(request))
    print("-" * 20)


log_handler = LogHandler()
authentication_handler = AuthenticationHandler()
authorization_handler = AuthorizationHandler()
default_handler = DefaultHandler()

log_handler.set_next(authentication_handler).set_next(authorization_handler).set_next(
    default_handler
)

client(log_handler, {"authenticated": False, "role": "admin"})
client(log_handler, {"authenticated": True, "role": "guest"})
client(log_handler, {"authenticated": True, "role": "admin"})
