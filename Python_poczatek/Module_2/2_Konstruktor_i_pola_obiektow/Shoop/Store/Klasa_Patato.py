class Potato:

   def __init__(self, kind, size, price):
       self.kind = kind
       self.size = size
       self.price = price

   def total_price_potato(self, weight_potato):
        return self.price * weight_potato