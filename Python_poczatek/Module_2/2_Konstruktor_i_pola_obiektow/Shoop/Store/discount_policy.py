
class DiscountPolicy:

    def apply_discount(self, order):
        return order

class PercentageDiscount(DiscountPolicy):

    CONSTANT_CUSTOMER = 0.05

    def __init__(self, percent_discount=None):
        if percent_discount is None:
            self.percent_discount = PercentageDiscount.CONSTANT_CUSTOMER
        self.percent_discount = percent_discount

    def apply_discount(self, order):
        return order - (order * self.percent_discount)
class AbsoluteDiscount(DiscountPolicy):

    CHRISMAS_DISCOUNT = 20

    def __init__(self, value_discount=None):
        if value_discount is None:
            self.value_discount = AbsoluteDiscount.CHRISMAS_DISCOUNT
        self.value_discount = value_discount

    def apply_discount(self, order):
        result = order - self.value_discount
        if result > 0:
            return result
        else:
            print(f"Zbyt niska kwota zamówienia aby naliczyć rabat:")
            return order