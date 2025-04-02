from abc import ABC, abstractmethod
from datetime import datetime


class Memento(ABC):  # Memento

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def get_datetime(self):
        pass


class TextEditorMemento(Memento):  # Concrete memento

    def __init__(self, data: str):
        self._data = data
        self._datetime = datetime.now()

    def get_data(self):
        return self._data

    def get_datetime(self):
        return self._datetime

    def get_full_info(self):
        return f"{self._data} / {self._datetime}"


class TextEditor:  # Originator

    def __init__(self):
        self._content = None

    def write(self, content: str):
        self._content = content

    def save(self) -> Memento:
        if self._content is None:
            print("Cannot saving empty content")
            return None
        return TextEditorMemento(self._content)

    def restore(self, memento: Memento):
        self._content = memento.get_data()

    def get_content(self):
        return self._content


class TextEditorHistory:  # Caretaker

    def __init__(self, text_editor: TextEditor):
        self._mementos = []
        self._text_editor = text_editor

    def save(self):
        self._mementos.append(self._text_editor.save())

    def undo(self):
        if not self._mementos:
            return None
        memento = self._mementos.pop()
        self._text_editor.restore(memento)

    def show_history(self):
        print("All history:")
        for memento in self._mementos:
            print("\t", memento.get_full_info())


# Client
text_editor = TextEditor()
text_editor_history = TextEditorHistory(text_editor)

text_editor.write("This is first text")
text_editor_history.save()
print("Current content: ", text_editor.get_content(), "\n")

text_editor.write("This is second edit")
text_editor_history.save()
print("Current content: ", text_editor.get_content(), "\n")

text_editor.write("This is third edit without saving")
print("Current content: ", text_editor.get_content(), "\n")

text_editor_history.show_history()

text_editor_history.undo()
print("Current content: ", text_editor.get_content(), "\n")

text_editor_history.undo()
print("Current content: ", text_editor.get_content(), "\n")
