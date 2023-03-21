from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order, ExpressOrder
from Store.product_and_other import Product, ExpiringProduct
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator
from Store.date_generator import generator_order

import random


def run_example():

    imie = "Daniel"
    nazwisko = "Iwanowski"
    new_order_list = generator_order(15)
    new_order = ExpressOrder(
        first_name=imie,
        second_name=nazwisko,
        position_list=new_order_list,
        discount_policy="normal_customer",
        delivery="24.03.2023"
        )
    print(new_order)



if __name__ == "__main__":

    run_example()
