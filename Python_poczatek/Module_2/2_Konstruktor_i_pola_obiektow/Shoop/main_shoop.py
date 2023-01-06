from Store.klasa_Apple import Apple
from Store.Klasa_Patato import Potato
from Store.order_and_other import Order, generator_order
from Store.product_and_other import Product



def run_example():

    green_apple = Apple(kind="Green", size="Medium", price=3.99)
    red_apple = Apple(kind="Red", size="Big", price=3.29)
    yellow_apple = Apple(kind="Yellow", size="Medium", price=4.49)
    print(red_apple)
    print(green_apple)
    print(yellow_apple)

    print(f"\t")
    print("-" * 20)

    young_potato = Potato(kind="Young", size="Small", price=4.68)
    old_poatato = Potato(kind="Old", size="Big", price=2.99)
    print(young_potato)
    print(old_poatato)

    print(f"\t")
    print("-" * 20)

    eny_product = Product(name="Butter", cathegory="food", price=5.29)
    print(eny_product)
    cookies = Product(name="Cookies", cathegory="Sweets", price=7.99)
    cookies.print_product()

    print(f"\t")
    print("-" * 20)

    empty_order = Order(first_name="Daniel", second_name="Iwanowski")
    eny_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])
    print(empty_order)
    print(eny_order)

    print(f"\t")
    print("-" * 20)

    first_order = Order(first_name="Daniel", second_name="Iwanowski", products=[cookies])
    first_order.prind_order()

    print(f"\t")
    print("-" * 20)

    eny_order = generator_order()
    eny_order.prind_order()


if __name__ == "__main__":
    run_example()