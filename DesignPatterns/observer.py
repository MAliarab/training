from abc import ABC, abstractmethod


class StockCountNotification(ABC):

    @abstractmethod
    def update(self, product_title: str, product_stock_count: int):
        pass


class UserStockCountNotification(StockCountNotification):

    def update(self, product_title: str, product_stock_count: int):
        if product_stock_count > 0:
            print(f"Notify users: product {product_title} is now available")


class SellerStockCountNotification(StockCountNotification):

    def update(self, product_title: str, product_stock_count: int):
        if product_stock_count == 0:
            print(f"Notify sellers: product {product_title} is out of stock")


class UpdateProduct(ABC):

    @abstractmethod
    def add_subscriber(self, subscriber: StockCountNotification):
        pass

    @abstractmethod
    def remove_subscriber(self, subscriber: StockCountNotification):
        pass

    @abstractmethod
    def _notify_subscribers(self, product_title: str, product_stock_count: int):
        pass


class UpdateDigitalProduct(UpdateProduct):

    def __init__(self):
        self._subscribers = []

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def _notify_subscribers(self, product_title, product_stock_count):
        for sub in self._subscribers:
            sub.update(product_title, product_stock_count)

    def update(self, product_data: dict):
        if "stock_count" in product_data:
            self._notify_subscribers(product_data["title"], product_data["stock_count"])


# Client
user_notif = UserStockCountNotification()
seller_notif = SellerStockCountNotification()

update_digital_product = UpdateDigitalProduct()
update_digital_product.add_subscriber(user_notif)
update_digital_product.add_subscriber(seller_notif)

update_digital_product.update({"title": "Mobile 1", "stock_count": 3})
update_digital_product.update({"title": "Mobile 1", "stock_count": 0})
