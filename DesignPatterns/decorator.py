"""
This is a non pythonic implementation (Global)
"""

from abc import ABC, abstractmethod


class Page(ABC):

    @abstractmethod
    def show_page(self):
        pass


class AdminPage(Page):

    def show_page(self):
        return "Welcome to admin page"


class PublicPage(Page):

    def show_page(self):
        return "Welcome to public page"


class PageDecorator(Page):

    def __init__(self, component: Page):
        self._component = component

    @abstractmethod
    def show_page(self):
        pass


class AuthPageDecorator(PageDecorator):

    def show_page(self):
        return f"Authentication process: {self._component.show_page()}"


def client(page: Page):
    print(page.show_page())
    print("-" * 20)


client(PublicPage())
client(AuthPageDecorator(AdminPage()))
