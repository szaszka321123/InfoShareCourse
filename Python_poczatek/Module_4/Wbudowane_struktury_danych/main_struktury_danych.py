from Zadania import int_oraz_float
import math


def run_example():
    name = input(f"Podaj swoje imię przybyszu: ")
    surname = input(f"Podaj swoje nazwisko przybyszu: ")

    clear_name = name.strip()
    clear_surname = surname.strip()

    print(f"Witaj {clear_name} {clear_surname}")




if __name__ == "__main__":
    run_example()