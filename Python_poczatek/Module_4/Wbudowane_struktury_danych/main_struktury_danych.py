from Zadania import int_oraz_float
import math


def run_example():
    first_float = int_oraz_float.draw_float_type()
    second_float = int_oraz_float.draw_float_type()
    third_float = int_oraz_float.draw_float_type()
    fourth_float = int_oraz_float.draw_float_type()
    fifth_float = int_oraz_float.draw_float_type()
    sixth_float = int_oraz_float.draw_float_type()

    first_int = int_oraz_float.draw_int_type()
    second_int = int_oraz_float.draw_int_type()
    third_int = int_oraz_float.draw_int_type()

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




if __name__ == "__main__":
    run_example()