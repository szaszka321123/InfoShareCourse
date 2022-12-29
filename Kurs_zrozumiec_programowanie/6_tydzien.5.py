                                                # Zad_1 "Funkcje"

# def pole_prostokata(dlugi_bok, krotki_bok):
#     obliczenie = dlugi_bok * krotki_bok
#     return int(obliczenie)
#
# def boki_int(message):
#     wczytaj = input(message)
#     return int(wczytaj)
#
# pierwszy_bok = boki_int(f"Podaj długość pierwszego boku: ")
# drugi_bok = boki_int(f"Podaj długość drugiego boku: ")
#
# wynik = pole_prostokata(pierwszy_bok, drugi_bok)
# print(wynik)

                                                # Zad 2 "Funkcje"

# def average_speed(time, distance):
#     speed = (time / 60) * distance
#     return int(speed)
#
# def input_system(message):
#     input_result = input(message)
#     return float(input_result)
#
# run_distance = input_system(f"Podaj odległośc w km jaką przebiegłeś: ")
# run_time = input_system(f"Podaj czas w minutach ile ci to zajeło: ")
# bike_distance = input_system(f"Podaj odległość jaką przejechałeś na rowerze: ")
# bike_time = input_system(f"Podaj czas w minutach ile Ci to zajeło: ")
# car_distance = input_system(f"Podaj odległość w km jaką przejechałeś:")
# car_time = input_system(f"Podaj czas w minutach ile Ci to zajeło: ")
#
# result_run = average_speed(run_distance, run_time)
# result_bike = average_speed(bike_distance, bike_time)
# result_car = average_speed(car_distance, car_time)
#
# print(f"Twoja średnia prędkość biegu to {result_run}")
# print(f"Twoja średnia prędkość na rowerze to {result_bike}")
# print(f"Twoja średnia prędkość jazdy autem to {result_car}")

                                                # Zad 3 "Funkcje"

# def ask_user():
#     while True:
#         index_user = input("Wypisz kategorię swoich wydatków lub wcisnij x aby zakończyć wprowadzanie:  ")
#         if index_user == "x":
#             print(f"Twoja lista kategorii wraz z przypisanymi do niej wartościami: \n{expenses}")
#             break
#         letter_user = float(input(f"Podaj ile zł wydajesz miesięcznie na {index_user}: "))
#         expenses[index_user] = letter_user
#
# def user_choose_result():
#     choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
#     print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
#     while choose_category != "x":
#         choose_category = input(
#             "Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić lub wciśnij x, aby zakończyć : ")
#         while choose_category not in percent_valumen and choose_category != "x":
#             print(f"Taka kategoria nie istnieje wbyierz inną")
#             choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
#         if choose_category != "x":
#             print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
#         else:
#             print(f"Dziekujemy i zapraszamy ponownie!!")
#
# def most_important_category_result():
#     most_important_category = None
#     most_percent = 0
#     for category, percent in percent_valumen.items():
#         if percent > most_percent:
#             most_percent = percent
#             most_important_category = category
#     if most_important_category is not None:
#         print(f"Najwięcej wydajesz na {most_important_category} czyli {most_percent:.2f}%")
#
#
#
# print("Witaj obliczymy twoj budrzet domowy, Zaczynajmy!!")
# expenses = {}
# ask_user()
#
#
# expenses_sum = 0
# for expense in expenses.values():
#     expenses_sum += expense
#
# walumen = 0
# percent_valumen = {}
# for name, valumen in expenses.items():
#     percent_index = valumen / expenses_sum * 100
#     percent_valumen[name] = percent_index
#
# expenses_keys = list(percent_valumen.keys())
#
# most_important_category_result()
# user_choose_result()

                                        # Zad_1 "Argumenty pozycyjne i nazwane"

# def average_speed(time, distance):
#     speed = (time / 60) * distance
#     return int(speed)
#
# def input_system(message):
#     input_result = input(message)
#     return float(input_result)
#
# run_distance = input_system(f"Podaj odległośc w km jaką przebiegłeś: ")
# run_time = input_system(f"Podaj czas w minutach ile ci to zajeło: ")
# bike_distance = input_system(f"Podaj odległość jaką przejechałeś na rowerze: ")
# bike_time = input_system(f"Podaj czas w minutach ile Ci to zajeło: ")
# car_distance = input_system(f"Podaj odległość w km jaką przejechałeś:")
# car_time = input_system(f"Podaj czas w minutach ile Ci to zajeło: ")
#
# result_run = average_speed(distance=run_distance, time=run_time)
# result_bike = average_speed(distance=bike_distance, time=bike_time)
# result_car = average_speed(distance=car_distance, time=car_time)
#
# print(f"Twoja średnia prędkość biegu to {result_run}")
# print(f"Twoja średnia prędkość na rowerze to {result_bike}")
# print(f"Twoja średnia prędkość jazdy autem to {result_car}")

                                            #Zad_1 "Parametry domyślne"

# def number_range(range=0.1):
#     range_plus = number + (range * number)
#     range_minus = number - (range * number)
#     return range_plus, range_minus
#
#
# number = float(input(f"Podaj dowolną liczbę: "))
#
# plus_number_range, minus_number_range = number_range()
# print(f"Zakres 10% liczby {number} to {plus_number_range}, {minus_number_range}")

                                            #Zad 2 "Parametry domyśln
# def add_person_to_list(name, list_of_name=None):
#     if list_of_name is None:
#         list_of_name = []
#         list_of_name.append(name)
#     return list_of_name
#
#
# name = None
# Lista_osob = []
# while name != "x":
#     name = input("Podaj imię które chcesz dodać do listy lub wciśnij x: ")
#     if name != "x":
#         Lista_osob += add_person_to_list(name)
# else:
#     print(Lista_osob)
