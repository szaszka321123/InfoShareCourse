# 3 tydzień

                                    # zad 1 "typy inf oraz float"

# print("Witaj sprawdzmy gdzie są najtańsze jabłka!!")
#
# apple_biedronka = input(" Podaj cenę jabłek w Biedronce (Kg): ")
# apple_lidl = input(" Podaj cenę jabłek w Lidlu (Kg): ")
# apple_zabka = input(" Podaj cenę jabłek w Żabce (Kg): ")
#
# biedronka_price = float(apple_biedronka)
# lidl_price = float(apple_lidl)
# zabka_price = float(apple_zabka)
#
# price_min = min(biedronka_price, lidl_price, zabka_price)
# price_max = max(biedronka_price, lidl_price, zabka_price)
#
# print("Najtańsze jabłka ze wszystkich sklepów kosztują: " + str(price_min) + " zl " )
# print("Najdroższe jabłka ze wszystkich sklepów kosztują: " + str(price_max) + " zl " )

                                    # zad 1 "Typ str, czyli napisy"

# Unowoczesnienie programu obliczania lokaty w banku ( Compilte)

                                    # zad 2 "Typ str, czyli napisy"

# user_name = input("Witaj , podaj swoję imię: ")
# print(f"Twoję imię posiada {len(user_name)} liter! ")

                                    # zad 3 "Typ str, czyli napisy"

# user_life_location = input("Witaj, gdzie mieszkasz?: ")
# print(f"O proszę!!Jak miło, że mieszkasz : {user_life_location.title()}")

                                    # zad 4 "Typ str, czyli napisy"

# ford = "ab100100"
# audi = "EEE 123123"
# citroen = "Zk-300300"
# honda = "AB210210"
#
# print(f"Ford:" ford.upper(),"\n Audi:" audi.upper().replace(' ',''),"\n Citroen: "citroen.upper().replace('-', ''),"\n Honda: "honda.upper()")

                                    # zad 1 "Typ listy"

# fovorite_sports = [
#     "tennis",
#     "volleyboll",
#     "mma",
#     "ksw",
#     "skiing"
# ]
# print(fovorite_sports)
# print(f"Ulubionym moim sportem jest: ", fovorite_sports[0])
# print(f"Najmniej ulubiony sport to : ", fovorite_sports[-1])
#
# fovorite_sports[2] = "baskedball"
# print(fovorite_sports)

                                    # zad 2 "Typ listy"

# favorite_meals = []
#
# first_meals = input("Podaj nazwę swojej ulubionej potrawy: ")
# favorite_meals.append(first_meals)
# second_meals = input("Podaj nazwę swojej drugiej ulubionej potrawy: ")
# favorite_meals.append(second_meals)
# third_meals = input("Podaj nazwę swojej trzeciej ulubionej potrawy: ")
# favorite_meals.append(third_meals)
#
# print("Twoje ulubione potrawy w kolejności to: ", favorite_meals)


                                    # zad 3 "Typ listy"
#
# user_phon_number = input("Podaj swój numer telefonu: ")
# user_phon_number = user_phon_number.replace(' ', '')
# user_phon_number = user_phon_number.replace('-', '')
# show_digits = user_phon_number[:6]
# shadow_digits = len(user_phon_number) - 6
# private_digits = "-" * shadow_digits
# anonymous_number = show_digits + private_digits
# print(f"Zanonimizowany numer ktory podales to: ",anonymous_number)

                                    # zad 1 " Typ dict, czyli słownik"

# show_retings = {
#     "Język Polski": 3,
#     "Język Angielski": 4,
#     "Metematyka": 5,
#     "WF": 6,
#     "Geografia": 4,
#     "Historia": 5
# }
# print(show_retings)

                                    # zad 2 " Typ dict, czyli słownik"

# my_family = {
#     "Ja": {
#         "Imię": "Daniel",
#         "Nazwisko": "Iwanowski",
#         "Data Urodzenia" : "02.07.1997"
#     },
#     "Tata": {"Imię": "Mietek",
#              "Nazwisko": "Iwanowski",
#              "Data Urdzoenia": "04.01.1977"
#     },
#     "Mama": {"Imię": "Ewa",
#              "Nazwisko": "Iwanowskia",
#              "Data Urodzenia": "12.12.1979"
#     }
# }
# print(my_family["Mama"])

                                    # zad 3 " Typ dict, czyli słownik"
# expenses = {}
#
# print("Witaj obliczymy twoj budrzet domowy, Zaczynajmy!!")
#
# food = float(input("Podaj ile zł wydajesz miesięcznie na jedzenie: "))
# expenses["food_sum"] = food
# entertainment = float(input("Podaj ile zł wydajesz miesięcznie na rozrywkę : "))
# expenses["entertainment_sum"] = entertainment
# fees = float(input("Podaj ile zł wydajesz miesięcznie na opłaty : "))
# expenses["fees_sum"] = fees
# others = float(input("Podaj ile zł wydajesz miesięcznie na inne rzeczy : "))
# expenses["others_sum"] = others
#
# expenses_values = list(expenses.values())
# expenses_sum = sum(expenses_values)
#
# expenses_precent = {}
#
# percent_food = food / expenses_sum * 100
# expenses_precent["food"] = percent_food
# percent_entertainment = entertainment / expenses_sum * 100
# expenses_precent["entertainment"] = percent_entertainment
# percent_fees = fees / expenses_sum * 100
# expenses_precent["fees"] = percent_fees
# percent_others = others / expenses_sum * 100
# expenses_precent["others"] = percent_others
#
# expenses_keys = list(expenses_precent.keys())
# print(f"Lista kategori: ", expenses_keys)
#
# choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
# print(f"Procent wydatków kategorii  {choose_category} wynosi: {expenses_precent[choose_category]:.2f}%")







