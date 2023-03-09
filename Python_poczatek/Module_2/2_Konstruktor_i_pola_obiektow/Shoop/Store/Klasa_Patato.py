class Potato:

   def __init__(self, kind, size, price, weight_potato):
       self.weight_potato = weight_potato
       self.kind = kind
       self.size = size
       self.price = price

   def total_price_potato(self):
        return self.price * self.weight_potato
   def __repr__(self):
       return f"Rodzaj ziemniaków: {self.kind} \n Rozmiar: {self.size} \n " \
              f"Cena za Kg: {self.price} \n Całkowiny koszt: {self.total_price_potato()}"
