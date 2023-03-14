from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order
from Store.product_and_other import Product
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator
import random
def sort_list(order):
    return order.total_price

def run_example():
    def generator_order():
        position_list = []
        for eny_number in range(10):
            name_product = f"Produkt {eny_number}"
            cathegory = "Inne"
            product_number = random.randint(1, 10)
            new_product = Product(name=name_product, cathegory=cathegory, price=product_number)
            quantity_number = random.randint(1, 5)
            position_list.append(OrderElement(product=new_product, quantity=quantity_number))

        return position_list

    position_list = generator_order()
    new_order = Order(first_name="Daniel", second_name="Iwanowski", positions_list=position_list)
    constant_order = Order(first_name="Daniel", second_name="Iwanowski", positions_list=position_list, discount_policy="constant_customer")
    chrismas_order = Order(first_name="Daniel", second_name="Iwanowski", positions_list=position_list, discount_policy="chrismas_customer")

    print(new_order)
    print(new_order)
    print(constant_order)
    print(chrismas_order)

if __name__ == "__main__":

    run_example()
