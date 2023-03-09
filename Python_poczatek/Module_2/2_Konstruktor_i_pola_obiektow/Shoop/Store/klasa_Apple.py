class Apple:

    def __init__(self, kind, size, price, weight):
        self.weight = weight
        self.kind = kind
        self.size = size
        self.price = price


    def total_price_apple(self):
        return self.price * self.weight
    def __repr__(self):
        return f"Rodzaj jabłek: {self.kind} \n Rozmiar jabłek: {self.size} \n Cena za Kg: {self.price} \n Cena zamówionych jabłek: {self.total_price_apple()}"
