import random

def name_and_surname():
    name = input(f"Podaj swoje imię przybyszu: ")
    surname = input(f"Podaj swoje nazwisko przybyszu: ")

    clear_name = name.strip()
    clear_surname = surname.strip()

    print(f"Witaj {clear_name} {clear_surname}")


def draw_id():
    new_id = str(random.randint(1, 10000))
    if len(new_id) < 5:
        new_id = new_id.zfill(5)

    return new_id









