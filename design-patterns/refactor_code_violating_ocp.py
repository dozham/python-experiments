## Refactor the following code violating OCP

# class DiscountCalculator:
#     def calculate_discount(self, customer_type: str, amount: float) -> float:
#         if customer_type == "regular":
#             return amount * 0.1  # 10% discount
#         elif customer_type == "premium":
#             return amount * 0.2  # 20% discount
#         else:
#             return 0.0  # No discount
#

from abc import ABC, abstractmethod
from typing import override

# Here's version 1: 
def version1():
    class BaseDiscountCalculator(ABC): # Having base class as an interface disallows people unintentionally using this class, but it lacks a NoDiscount class
        @abstractmethod
        def calculate_discount(self, amount: float) -> float:
            pass
            # return 0 * amount

    class RegularDiscountCalculator(BaseDiscountCalculator):
        @override
        def calculate_discount(self, amount: float) -> float:
            return amount * 0.1

    class PremiumDiscountCalculator(BaseDiscountCalculator):
        @override
        def calculate_discount(self, amount: float) -> float:
            return amount * 0.2

    class NoDiscountCalculator(BaseDiscountCalculator):
        @override
        def calculate_discount(self, amount: float) -> float:
            return 0.0


# Here's version 2: 
# which also uses dependency injection / IoC for dynamically swappable discount strategy
def version2():
    class DiscountStrategy(ABC):
        @abstractmethod
        def calculate_discount(self, amount: float) -> float:
            pass

    class NoDiscountStrategy(DiscountStrategy):
        @override
        def calculate_discount(self, amount: float) -> float:
            return 0.0

    class RegularDiscountStrategy(DiscountStrategy):
        @override
        def calculate_discount(self, amount: float) -> float:
            return 0.1 * amount

    class PremiumDiscountStrategy(DiscountStrategy):
        @override
        def calculate_discount(self, amount: float) -> float:
            return 0.2 * amount

    class DiscountCalculator():
        def __init__(self, strategy: DiscountStrategy):
            self.strategy = strategy

        def calculate_discount(self, amount: float) -> float:
            return self.strategy.calculate_discount(amount)


