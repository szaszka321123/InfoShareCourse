
                                               #Zad_1 " Pętla While"
# even_number = int(input(f"Podaj dowolną liczbę parzystą: "))
# try_number = 1
# while even_number % 2 != 0 and try_number < 10:
#     if even_number % 2 != 0 and try_number < 10:
#         print(f"{even_number} nie jest liczbą parzystą")
#     even_number = int(input(f"Podaj dowolną liczbę parzystą: "))
#     try_number += 1
#     if try_number == 10:
#         print(f"Wykorzystałeś limit prób")


                                                #Zad 2 " Pętla While"

# user_number = input(f"Podaj swój numer telefonu: ")
# user_number = user_number.replace(" ", "")
# user_number = user_number.replace("-", "")
#
# number_format = ""
# index_format = 0
#
# while index_format < len(user_number):
#     if index_format % 3 == 0 and index_format != 0:
#         number_format += "-"
#     number_format += user_number[index_format]
#     index_format += 1
# print(number_format)

                                                #Zad 3 " Pętla While"

# dishes_list = input("Podaj listę swoich ulubionych potraw wypisując je po przecinku: ")
# main = dishes_list.split(",")
# number = 0
# index_dishes = 1
#
# while index_dishes <= len(main):
#     print(f"Potrawa na miejscu {index_dishes} to {main[number]}")
#     index_dishes += 1
#     number += 1
# print("Niezła lista xd")

                                                # Zad_1 " Pętla For"

# user_action = input("Podaj swoją ocenę lub wciśnij przycisk x aby obliczyć średnią z podanych wcześniej ocen: ")
# if user_action != "x":
#     grades_list = []
#     while user_action != "x":
#         if int(user_action) <= 6 and int(user_action) != 0:
#             grades_list += user_action
#             user_action = input("Podaj swoją ocenę lub wciśnij przycisk x aby obliczyć średnią z podanych wcześniej ocen: ")
#         else:
#             print("Taka ocena nie istenieje")
#             user_action = input("Podaj swoją ocenę lub wciśnij przycisk x aby obliczyć średnią z podanych wcześniej ocen: ")
#     print(f"Twoja lista ocen którą podałęś/aś: {grades_list}")
#
#     avergage_grade = 0
#     for grade in grades_list:
#         avergage_grade += int(grade)
#     result = avergage_grade / len(grades_list)
#     print(f"Twoja średnia z podanych ocen to: {result:.2f}")
# else:
#     print("No co ty nie podałeś przecież rzadnmych ocen xD")

                                                # Zad 2 " Pętla For"

# user_number = input(f"Podaj swój numer telefonu: ")
# user_number = user_number.replace(" ", "")
# user_number = user_number.replace("-", "")
#
# number_format = ""
#
# for index, latter in enumerate(user_number):
#     if index % 3 == 0 and index != 0:
#         number_format += "-"
#     number_format += latter
# print(number_format)


                                                # Zad 3 " Pętla For"
#
# print("Witaj obliczymy twoj budrzet domowy, Zaczynajmy!!")
# index_user = input("Wypisz kategorię swoich wydatków:  ")
# letter_user = float(input(f"Podaj ile zł wydajesz miesięcznie na {index_user}: "))
#
#
# expenses = {}
# expenses[index_user] = letter_user
#
# while index_user != "x":
#     index_user = input("Wypisz kategorię swoich wydatków lub wcisnij x aby zakończyć wprowadzanie:  ")
#     if index_user != "x":
#         letter_user = float(input(f"Podaj ile zł wydajesz miesięcznie na {index_user}: "))
#         expenses[index_user] = letter_user
# print(f"Twoja lista kategorii wraz z przypisanymi do niej wartościami: \n{expenses}")
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
# most_important_category = None
# most_percent = 0
# for category, percent in percent_valumen.items():
#     if percent > most_percent:
#         most_percent = percent
#         most_important_category = category
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} czyli {most_percent:.2f}%")
#
# print(f"\nLista kategori: ", expenses_keys)
# choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
# print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
# while choose_category != "x":
#     choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić lub wciśnij x, aby zakończyć : ")
#     while choose_category not in percent_valumen and choose_category != "x":
#         print(f"Taka kategoria nie istnieje wbyierz inną")
#         choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
#     if choose_category != "x":
#         print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
#     else:
#         print(f"Dziekujemy i zapraszamy ponownie!!")


                                                # Zad_1 "Petla for in range"

# user_phon_number = input("Podaj swój numer telefonu: ")
# user_phon_number = user_phon_number.replace(' ', '')
# user_phon_number = user_phon_number.replace('-', '')
#
# show_digits = user_phon_number[:6]
# shadow_digits = len(user_phon_number) - 6
# private_digits = "-" * shadow_digits
# anonymous_number = show_digits + private_digits
# print(f"Zanonimizowany numer ktory podales to: ",anonymous_number)
#
# for digit in range(10):
#     digit_number = user_phon_number.count(str(digit))
#     print(f"Cyfra {digit} wystepuje: {digit_number} razy")

                                                # Zad 2 "Petla for in range"


# kredyt_price = float(input("Podaj kwotę kredytu: "))
# percent_kredyt = float(input("Podaj oprocentowanie kredttu jakie cię interesuje: "))
# czas_kredytowania = float(input("Podaj czas kredytowania w latach: "))
# poczatkowe_koszta = float(input(f"Jakie sa koszta początkowe: "))
#
# moth_paid = 12 * czas_kredytowania
# rata_kredytu = (kredyt_price * percent_kredyt/100)/12 + kredyt_price / moth_paid
# kapital_splacony_miesiecznie = kredyt_price / moth_paid
# pozostaly_kapital = kredyt_price - (moth_paid - 1) * kapital_splacony_miesiecznie
# rata = (pozostaly_kapital * percent_kredyt / 100) / 12 + kapital_splacony_miesiecznie
#
#
# for index in range(1, int(moth_paid) +1):
#     kapital_do_zaplacenia = index * rata

                                                # Zad_1 "Komedy break i Continue"

# school_subject_list = []
#
# print(f"Witaj sprawdzmy czy zdałeś do następnej klasy xd")
#
# maths = float(input("Podaj swoją ocenę z Matematyki: "))
# physic = float(input("Podaj swoją ocenę z fizyki: "))
# Wf = float(input("Podaj swoją ocenę z WF: "))
# Biology = float(input("Podaj swoją ocenę z Biologii: "))
# Nature = float(input("Podaj swoją ocenę z Przyrody: "))
# History = float(input("Podaj swoją ocenę z Histori: "))
#
# school_subject_list.append(maths)
# school_subject_list.append(physic)
# school_subject_list.append(Wf)
# school_subject_list.append(Biology)
# school_subject_list.append(Nature)
# school_subject_list.append(History)
#
# for number in school_subject_list:
#     if number == 1:
#         print(f"Przykro mi masz jedynkę i niezdałeś")
#         break
# else:
#     print(f"Gratulacje nie masz jedynki zdałeś")

                                               # Zad 2 "Komedy break i Continue"

# print("Witaj obliczymy twoj budrzet domowy, Zaczynajmy!!")
#
# expenses = {}
#
# while True:
#     index_user = input("Wypisz kategorię swoich wydatków lub wcisnij x aby zakończyć wprowadzanie:  ")
#     if index_user == "x":
#         print(f"Twoja lista kategorii wraz z przypisanymi do niej wartościami: \n{expenses}")
#         break
#     letter_user = float(input(f"Podaj ile zł wydajesz miesięcznie na {index_user}: "))
#     expenses[index_user] = letter_user
# print(f"Twoja lista kategorii wraz z przypisanymi do niej wartościami: \n{expenses}")
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
# most_important_category = None
# most_percent = 0
# for category, percent in percent_valumen.items():
#     if percent > most_percent:
#         most_percent = percent
#         most_important_category = category
# if most_important_category is not None:
#     print(f"Najwięcej wydajesz na {most_important_category} czyli {most_percent:.2f}%")
#
# print(f"\nLista kategori: ", expenses_keys)
# choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
# print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
# while choose_category != "x":
#     choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić lub wciśnij x, aby zakończyć : ")
#     while choose_category not in percent_valumen and choose_category != "x":
#         print(f"Taka kategoria nie istnieje wbyierz inną")
#         choose_category = input("Wybierz kategorię jakiej procent łącznych wydatków chcesz sprawdzić : ")
#     if choose_category != "x":
#         print(f"Procent wydatków kategorii  {choose_category} wynosi: {percent_valumen[choose_category]:.2f}%")
#     else:
#         print(f"Dziekujemy i zapraszamy ponownie!!")

                                               # Zad 3 "Komedy break i Continue"
#
# list_of_numbers = [1, 2, 22, 562, 421, 5673, 2421, 424, 115, 125, 552, 1125, 5626, 122451, 552, 22155, 56216, 7211]
#
# for index, number in enumerate(list_of_numbers):
#     if number % 2 != 0:
#         print(number)
