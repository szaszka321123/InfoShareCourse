import random
import math
def draw_float_type():
    return random.uniform(-20, 20)

def draw_int_type():
    return random.randint(1, 10)


def int_float_run_example():

    first_float = draw_float_type()
    second_float = draw_float_type()
    third_float = draw_float_type()
    fourth_float = draw_float_type()
    fifth_float = draw_float_type()
    sixth_float = draw_float_type()

    first_int = draw_int_type()
    second_int = draw_int_type()
    third_int = draw_int_type()

    print(first_float)
    print(second_float)
    print(third_float)
    print(first_int)
    print(second_int)
    print(third_int)

    print(round(first_float))
    print(math.ceil(second_float))
    print(math.floor(third_float))

    print(fourth_float ** first_int)
    print(pow(fifth_float, second_int))
    print(math.pow(sixth_float, third_int))