from Store.order_and_other import ExpressOrder
from Store.date_generator import generator_order
from Store.discount_policy import PercentageDiscount, AbsoluteDiscount
from Store.order_and_other import ExpressOrder


def run_example():

    imie = "Daniel"
    nazwisko = "Iwanowski"
    new_order_list = generator_order(10)
    twenty_zloty_discount = AbsoluteDiscount(value_discount=20)
    ten_percent_discount = PercentageDiscount(percent_discount=0.1)


    new_order = ExpressOrder(
        first_name=imie,
        second_name=nazwisko,
        position_list=new_order_list,
        discount_policy=None,
        delivery="24.03.2023"
        )

    second_order = ExpressOrder(
        first_name=imie,
        second_name=nazwisko,
        position_list=new_order_list,
        discount_policy=twenty_zloty_discount,
        delivery="24.03.2023"
        )

    third_order = ExpressOrder(
        first_name=imie,
        second_name=nazwisko,
        position_list=new_order_list,
        discount_policy=ten_percent_discount,
        delivery="24.03.2023"
        )

    print(new_order)
    print(second_order)
    print(third_order)



if __name__ == "__main__":

    run_example()
