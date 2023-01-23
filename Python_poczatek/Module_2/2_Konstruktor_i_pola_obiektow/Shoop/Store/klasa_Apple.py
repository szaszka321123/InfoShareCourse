class Apple:

    def __init__(self, kind, size, price):
        self.kind = kind
        self.size = size
        self.price = price


    def total_price_apple(self, weight):
        return self.price * weight
