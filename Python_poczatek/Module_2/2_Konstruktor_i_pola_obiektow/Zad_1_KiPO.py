import random


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

        total_price = 0
        for product in products:
            if product is int:
                total_price += product
        self.total_price = total_price



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
    eny_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])
    print(empty_order)
    print(eny_order)

def print_product(message):
    print(f"Twój produkt to: {cookies.name} - Katergoria: {cookies.cathegory} - Cena jednostkowa: {cookies.price}")

cookies = Product(name="Cookies", cathegory="Sweets", price=7.99)

def prind_order(Order):
    print("-" * 20)
    print(f"Imię: {Order.first_name}")
    print(f"Nazwisko: {Order.second_name}")
    print(f"Lista produktów {Order.products}")
    print(f"Wartość zamówienia {Order.total_price}zł")
    for product in Order.products:
        print("\t", end="")
        print_product(product)
    print("-" * 20)



first_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])

def generator_order():
    number_order = random.randint(1, 20)
    for eny_number in range(number_order):
        product_number = random.randint(1, 10)
        product_list = []
        for product in range(product_number):
            new_product = f"Produkt {product}"
            product_list.append(new_product)
        new_order = Order(first_name="Imię klijęta", second_name="Nazwisko klijęta", products=product_list)

    return new_order


def run_example():
    eny_order = generator_order()
    prind_order(eny_order)


if __name__ == "__main__":
    zad_1_KiPO()
    print(f"\t")
    print("-" * 20)
    print_product(cookies)
    prind_order(first_order)
    run_example()


