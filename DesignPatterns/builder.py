from abc import ABC, abstractmethod


class Car:

    def __init__(self):
        self._wheel = None
        self._engine = None
        self._body = None

    def set_wheel(self, wheel: "Wheel"):
        self._wheel = wheel
        return self

    def set_engine(self, engine: "Engine"):
        self._engine = engine
        return self

    def set_body(self, body: "Body"):
        self._body = body
        return self

    def get_detail(self):
        print(f"Body: {self._body.shape}")
        print(f"Engine: {self._engine.hp}")
        print(f"Wheel: {self._wheel.size}")
        print("-" * 20)


class Body:
    shape = None


class Engine:
    hp = None


class Wheel:
    size = None


class AbstractBuilder(ABC):

    @abstractmethod
    def get_body(self):
        pass

    @abstractmethod
    def get_engine(self):
        pass

    @abstractmethod
    def get_wheel(self):
        pass


class BenzBuilder(AbstractBuilder):

    def get_body(self):
        body = Body()
        body.shape = "suv"

    def get_engine(self):
        engine = Engine()
        engine.hp = 300

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20


class BenzBuilder(AbstractBuilder):

    def get_body(self):
        body = Body()
        body.shape = "suv"
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 300
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 20
        return wheel


class BMWBuilder(AbstractBuilder):

    def get_body(self):
        body = Body()
        body.shape = "coupe"
        return body

    def get_engine(self):
        engine = Engine()
        engine.hp = 310
        return engine

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel


class Director:

    def __init__(self, builder: AbstractBuilder):
        self._builder = builder()

    def construct(self):
        car = Car()

        body = self._builder.get_body()
        car.set_body(body)

        engine = self._builder.get_engine()
        car.set_engine(engine)

        wheel = self._builder.get_wheel()
        car.set_wheel(wheel)

        return car


def client(builder: AbstractBuilder):
    director = Director(builder)
    car = director.construct()
    car.get_detail()


client(BenzBuilder)
client(BMWBuilder)
