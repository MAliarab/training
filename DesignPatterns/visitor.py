from abc import ABC, abstractmethod


class DiscountVisitor(ABC):  # Abstract visitor

    @abstractmethod
    def visit_digital(self, product: "DigitalProduct"):
        pass

    @abstractmethod
    def visit_clothing(self, product: "ClothingProduct"):
        pass


class WeekendDiscount(DiscountVisitor):  # Concrete visitor

    def visit_digital(self, product):
        discount = product.price * 0.05  # 5% off
        return product.price - discount

    def visit_clothing(self, product):
        discount = product.price * 0.07  # 7% off
        return product.price - discount


class Product(ABC):  # Abstract Element

    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    @abstractmethod
    def accept(self, discount_visitor: DiscountVisitor):
        pass


class DigitalProduct(Product):  # Concrete Element 1

    def accept(self, discount_visitor: DiscountVisitor):
        return discount_visitor.visit_digital(self)


class ClothingProduct(Product):  # Concrete Element 2

    def accept(self, discount_visitor: DiscountVisitor):
        return discount_visitor.visit_clothing(self)


# Client
weekend_discount = WeekendDiscount()

digital_product = DigitalProduct("Phone 1", 1000)
clothing_product = ClothingProduct("T-shirt 2", 130)

print(f"Original price of {digital_product.name} is ${digital_product.price}")
print(f'Discounted Price: " ${digital_product.accept(weekend_discount)} " ')

print(f"Original price of {clothing_product.name} is ${clothing_product.price}")
print(f'Discounted Price:  " ${clothing_product.accept(weekend_discount)} " ')
