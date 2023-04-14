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

def user_colors():
    the_best_user_colors = input(f"Witaj przybyszu, podaj swoje ulubione kolory oddzielając je tylko przecinkiem: ")
    result = the_best_user_colors.rfind("niebieski")
    if result > 0:
        return print(f"Wsrod twoich ulubionych kolorow znajduje sie koloro niebieski SUPER!!!")
    else:
        return print(f"Nie lubisz niebieskiego?")








