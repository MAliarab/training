from abc import ABC, abstractmethod


class Shape(ABC):  # Abstraction

    def __init__(self, color: "Color"):
        self.color = color

    @abstractmethod
    def show(self):
        pass


class Circle(Shape):  # Refined Abstraction 1

    def show(self):
        return self.color.paint("circle")


class Rectangle(Shape):  # Refined Abstraction 2

    def show(self):
        return self.color.paint("rectangle")


class Color(ABC):  # Implementation

    @abstractmethod
    def paint(self, obj):
        pass


class Red(Color):  # Concret implementation 1

    def paint(self, obj):
        return f"This is a red {obj}"


class Blue(Color):  # Concret implementation 2

    def paint(self, obj):
        return f"This is a blue {obj}"


def client(shape: Shape):
    print(shape.show())


client(Circle(Red()))
client(Rectangle(Blue()))
