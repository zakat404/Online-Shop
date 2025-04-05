from abc import ABC, abstractmethod
from online_shop.pricing import PricingRule

class Product(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_price(self) -> float:
        pass

class SimpleProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name)
        self.price = price

    def get_price(self) -> float:
        return self.price

class ProductGroup(Product):
    def __init__(self, name: str, products: list, pricing_rule: PricingRule):
        super().__init__(name)
        self.products = products
        self.pricing_rule = pricing_rule

    def get_price(self) -> float:
        return self.pricing_rule.calculate(self.products)
