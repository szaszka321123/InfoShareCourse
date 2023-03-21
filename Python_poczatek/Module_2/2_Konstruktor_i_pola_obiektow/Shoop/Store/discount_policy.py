
class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price

class PercentageDiscount(DiscountPolicy):

    def __init__(self, percent_discount=None):
        self.percent_discount = percent_discount

    def apply_discount(self, total_price):
        return total_price - (total_price * self.percent_discount)

class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, value_discount=None):
        self.value_discount = value_discount

    def apply_discount(self, total_price):
        result = total_price - self.value_discount
        if result > 0:
            return result
        else:
            print(f"Zbyt niska kwota zamówienia aby naliczyć rabat:")
            return total_price