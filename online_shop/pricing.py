from abc import ABC, abstractmethod

class PricingRule(ABC):
    @abstractmethod
    def calculate(self, products: list) -> float:
        pass

class DiscountPricingRule(PricingRule):
    def __init__(self, discount_percentage: float):
        self.discount_percentage = discount_percentage

    def calculate(self, products: list) -> float:
        total = sum(product.get_price() for product in products)
        discount = total * self.discount_percentage / 100
        return total - discount

class EveryNthFreePricingRule(PricingRule):
    def __init__(self, n: int):
        self.n = n

    def calculate(self, products: list) -> float:
        prices = [product.get_price() for product in products]
        total = sum(prices)
# количество бесплатных товаров
        count_free = len(prices) // self.n
# Выбираем самые дешёвые товары для бесплатного предоставления
        prices_sorted = sorted(prices)
        free_amount = sum(prices_sorted[:count_free])
        return total - free_amount
