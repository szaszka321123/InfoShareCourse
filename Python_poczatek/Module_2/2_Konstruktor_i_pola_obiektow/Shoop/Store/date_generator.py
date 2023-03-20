import random

from Store.order_and_other import Order
from Store.order_element import OrderElement
from Store.product_and_other import Product

MAX_QUANTITY = 10
MIN_QUANTITY = 1

MAX_UNIT_PRICE = 30
MIN_UNIT_PRICE = 1

def generator_order(number_of_products=None):
    if number_of_products is None:
        number_of_products = random.randint(1, Order.MAX_ORDER_ELEMENT_LIMIT)
    position_list = []
    for eny_number in range(number_of_products):
        name_product = f"Produkt {eny_number}"
        cathegory = "Inne"
        product_number = random.randint(MIN_UNIT_PRICE, MAX_UNIT_PRICE)
        new_product = Product(name=name_product, cathegory=cathegory, price=product_number)
        quantity_number = random.randint(MIN_QUANTITY, MAX_QUANTITY)
        position_list.append(OrderElement(product=new_product, quantity=quantity_number))

    return position_list
