class Product:

    def __init__(self, name, cathegory, price):
        self.price = price
        self.cathegory = cathegory
        self.name = name


class Order:

    def __init__(self, first_name, second_name, products=None):
        self.second_name = second_name
        self.first_name = first_name
        if products is None:
            products = []
        self.products = products

class Apple:

    def __init__(self, kind, size, price):
        self.kind = kind
        self.size = size
        self.price = price

class Potato:

   def __init__(self, kind, size, price):
       self.kind = kind
       self.size = size
       self.price = price


def zad_1_KiPO():

    eny_product = Product(name="Butter", cathegory="food", price=5.29)
    print(eny_product)

    green_apple = Apple(kind="Green", size="Medium", price=3.99)
    red_apple = Apple(kind="Red", size="Big", price=3.29)
    yellow_apple = Apple(kind="Yellow", size="Medium", price=4.49)
    print(red_apple)
    print(green_apple)
    print(yellow_apple)

    young_potato = Potato(kind="Young", size="Small", price=4.68)
    old_poatato = Potato(kind="Old", size="Big", price=2.99)
    print(young_potato)
    print(old_poatato)

    empty_order = Order(first_name="Daniel", second_name="Iwanowski")
    eny_order = Order(first_name="Daniel", second_name="Iwanowski", products=[green_apple])
    print(empty_order)
    print(eny_order)

if __name__ == "__main__":
    zad_1_KiPO()


