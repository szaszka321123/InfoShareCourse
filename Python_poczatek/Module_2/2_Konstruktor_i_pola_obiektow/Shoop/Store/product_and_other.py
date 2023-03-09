class Product:

    def __init__(self, name, cathegory, price):
        self.name = name
        self.cathegory = cathegory
        self.price = price



    def __str__(self):
        return f"Twój produkt to: {self.name} - Katergoria: {self.cathegory} - Cena jednostkowa: {self.price}/szt"



