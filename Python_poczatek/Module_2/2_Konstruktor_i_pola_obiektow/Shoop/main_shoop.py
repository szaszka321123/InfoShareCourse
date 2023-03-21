from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order
from Store.product_and_other import Product
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator
from Store.date_generator import generator_order

import random


def run_example():


    position_list = generator_order()
    new_order = Order(first_name="Daniel", second_name="Iwanowski", positions_list=position_list)
    print(new_order)

    new_order.position_list = generator_order(10)
    print(new_order)

    new_order.position_list = generator_order(1000)
    print(new_order)


if __name__ == "__main__":

    run_example()
