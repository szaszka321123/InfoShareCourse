from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order
from Store.product_and_other import Product, ExpiringProduct
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator
from Store.date_generator import generator_order

import random


def run_example():

    new_product = ExpiringProduct(name="Jar of ham", cathegory="food", price=12.29, year_of_production=2019, years_validity=11)
    new_product.does_expire(2032)



if __name__ == "__main__":

    run_example()
