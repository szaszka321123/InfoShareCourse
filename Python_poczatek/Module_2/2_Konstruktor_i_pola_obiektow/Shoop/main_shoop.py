from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order, generator_order
from Store.product_and_other import Product

def run_example():

    first_order = generator_order()
    print(first_order)
    second_order = generator_order()
    print(second_order)

if __name__ == "__main__":

    run_example()