from Zadania import int_oraz_float
import math
from Zadania import str_czyli_napis

def run_example():


    you = str_czyli_napis.name_and_surname()
    print(you)

    any_id = str_czyli_napis.draw_id()
    print(f" Twoje ID to: {any_id}")

    change_blue = str_czyli_napis.user_colors()
    print(change_blue)



if __name__ == "__main__":
    run_example()