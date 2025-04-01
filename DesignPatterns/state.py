from abc import ABC, abstractmethod


class OrderState(ABC):  # Abstract State

    def __init__(self):
        self.order_context = None

    def set_context(self, order: "OrderContext"):
        self.order_context = order

    @abstractmethod
    def prev_state(self):
        pass

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class NewOrder(OrderState):  # Concrete State 1

    def prev_state(self):
        print("Error: New order has no prev state !!!")

    def next_state(self):
        self.order_context.set_state(ProcessingOrder())

    def get_state(self):
        return "State 1: New Order"


class ProcessingOrder(OrderState):  # Concrete State 2

    def prev_state(self):
        self.order_context.set_state(NewOrder())

    def next_state(self):
        self.order_context.set_state(ShippingOrder())

    def get_state(self):
        return "State 2: Processing Order"


class ShippingOrder(OrderState):  # Concrete State 3

    def prev_state(self):
        self.order_context.set_state(ProcessingOrder())

    def next_state(self):
        self.order_context.set_state(DeliveredOrder())

    def get_state(self):
        return "State 3: Shipping Order"


class DeliveredOrder(OrderState):  # Concrete State 4

    def prev_state(self):
        self.order_context.set_state(ShippingOrder())

    def next_state(self):
        print("Error: Delivered order has no next state !!!")

    def get_state(self):
        return "State 4: Order Delivered"


class OrderContext:  # Context

    def __init__(self, state: OrderState):
        self.set_state(state)

    def set_state(self, state: OrderState):
        self._state = state
        self._state.set_context(self)

    def prev_state(self):
        self._state.prev_state()

    def next_state(self):
        self._state.next_state()

    def get_state(self):
        return self._state.get_state()


# Client
order_context = OrderContext(NewOrder())
print("Current state: ", order_context.get_state())

order_context.next_state()  # move to next state
print("Current state: ", order_context.get_state())

order_context.next_state()  # move to next state
print("Current state: ", order_context.get_state())

order_context.prev_state()  # back to prev state
print("Current state: ", order_context.get_state())

order_context.next_state()  # move to next state
print("Current state: ", order_context.get_state())

order_context.next_state()  # move to next state
print("Current state: ", order_context.get_state())

order_context.next_state()  # This will cuase error
print("Current state: ", order_context.get_state())
