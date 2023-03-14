from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order
from Store.product_and_other import Product
from Store.order_element import OrderElement
from Store.klasa_TaxCalculator import TaxCalculator

def sort_list(order):
    return order.total_price

def run_example():



    list_orders = []
    if list_orders is not None:
        for _ in range(5):
            list_orders.append(Order.generator_order())

    list_orders.sort(key=sort_list)
    for order in list_orders:
        print(order)


if __name__ == "__main__":

    run_example()
