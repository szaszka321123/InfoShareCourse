                                                #zad 1 "Porównanie i typ bool"

# apple_prize = float(input("Podaj cenę jabłek: "))
# bananas_prize = float(input("Podaj cenę bananów: "))
# carrot_prize = float(input("Podaj cenę marchwi: "))
#
# print(f"Wynik porównania jabłka = bananow: {apple_prize == bananas_prize}")
# print(f"Wynik porownania cen marchwi >= bananow:  {carrot_prize >= bananas_prize}")
# print(f"wynik porowanania marchwi != jabłek: {apple_prize != carrot_prize} ")

                                                #zad 2 "Porównanie i typ bool"

# shopping_list = input("Podaj wypisując po przecinku listę zakupów: ")
# lenght_list = 50 < len(shopping_list)
# print(f"Lista jest długa:  {lenght_list}")

                                                #zad 3 "Porównanie i typ bool"
#
# print("Oblicz z nami wartosc lokaty!")
#
# value = float(input(" Podaj wartosc w zlotowkach jaka chcesz wplacic na lokate w banku: "))
# percent = float(input(" Podaj oprocentowanie swojej lokaty: "))
# years = float(input(" Podaj w latach czas trwania: "))
#
# interest = (1 + percent/ 100)
#
# month_user = int(years) * 12
#
# locate_value = value * interest ** years
# locate_value_month = value * interest ** (years * 12)
#
# increase_10_percent = (value + (value * 0.1))
# value_min_10_percent = increase_10_percent < locate_value
#
# info = (f"Wartość twojej lokaty po {years} latach, czyli {month_user} miesiacach wynosi: {locate_value:.2f} zł")
# print(info)
# print(f"Czy wartość loakty po okresie {years} lat, wzrośnie o minimum 10%? : {value_min_10_percent}")

                                                #zad 1 "Instrukcja if/else"
#
# apple_prize = float(input("Podaj cenę jabłek: "))
# bananas_prize = float(input("Podaj cenę bananów: "))
# carrot_prize = float(input("Podaj cenę marchwi: "))
#
#
# if apple_prize == bananas_prize:
#     print(f"Jabłka oraz banany kosztują tyle samo")
# else:
#     if apple_prize < bananas_prize:
#         print(f"Banany są droższe niż jabłka")
#     else:
#         print(f"Banany są tańsze niż jabłka")
#
# if bananas_prize == carrot_prize:
#     print(f"Banany kosztują tyle co marchew")
# else:
#     if bananas_prize < carrot_prize:
#         print(f"Marchew jest droższa od bananów")
#     else:
#         print(f"Marchew jest tańsza od bananów")
#
# if apple_prize == carrot_prize:
#     print(f"Jabłka kosztują tyle co marchew")
# else:
#     if apple_prize < carrot_prize:
#         print(f"Jabłka są tańsze niż marchew ")
#     else:
#         print(f"Jabłka są droższe niż marchew")
#
# shopping_list = input("Podaj wypisując po przecinku listę zakupów: ")
# lenght_list = 50 < len(shopping_list)
# if lenght_list:
#     print(f"Twoja lista jest długa ")
# else:
#     print(f"Twoja lista jest raczej krótka")

                                                #zad 2 "Instrukcja if/else"
# niezrobione bo bezsensu xd

                                                #zad 3 "Instrukcja if/else"
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
# sum_list = sum(school_subject_list)
# average_grade = sum_list / 6
#
# print(f"Twoja średnia ocen to : {average_grade:.2f}")
#
# if 1 in school_subject_list:
#     if average_grade >= 3.5:
#         print(f"Masz jedną jedynkę , ale również średnią powyżej 3.5 więc zdajesz do następnej klasy")
#     else:
#         print(f"Posiadasz więcej niż jedną jedynkę lub masz jedną jedynkę i za niską średnią aby zdać")
# else:
#     print("Gratuluje zdałeś bez problemu ")

                                                #zad 4 "Instrukcja if/else"

# name = list(input("Witaj jak masz na imię?: "))
#
# last_latter = name[-1]
#
# if last_latter == "a":
#     print(f"Jesteś Kobietą , miło mi ")
# else:
#     print("Jesteś facetem")

                                                #zad 1 "operatory logiczne and/or/not"

# kredyt_price = float(input("Podaj kwotę kredytu: "))
# percent_kredyt = float(input("Podaj oprocentowanie kredttu jakie cię interesuje: "))
# wklad_wlasny = float(input("Podaj wartość wkładu własnego: "))
# czas_kredytowania = float(input("Podaj czas kredytowania w latach: "))
# przychod_miesieczny = float(input("Podaj przychód miesięczny: "))
# suma_miesiecznych_wydatkow = float(input("Podaj sumę swoich miesięcznych wydatków: "))
#
# rata_kredytu = (kredyt_price * percent_kredyt/100)/12 + kredyt_price / (czas_kredytowania * 12)
# dostepne_srodki = przychod_miesieczny - suma_miesiecznych_wydatkow
# wartosc_nieruchomosci = wklad_wlasny + kredyt_price
#
# print(f"Twoja miesięczna rata kredytu dla podanych watości wynosi {rata_kredytu:.2f}")
# procent_wkladu_do_nieruchomosci = (wklad_wlasny / wartosc_nieruchomosci) * 100
# print(f"Procentowy udział Twojego wkładu w nieruchomości wynosi: {procent_wkladu_do_nieruchomosci:.2f}%")
#
# if procent_wkladu_do_nieruchomosci > 20 and dostepne_srodki > (rata_kredytu + 1000) or 10 < procent_wkladu_do_nieruchomosci < 20 and dostepne_srodki > ( rata_kredytu + 2000):
#     print(f"Gratulację spełniasz warunki wzięcia kredytu!!")
# else:
#     print(f"Twój wkład wałsny jest za niski aby wziąć kredyt o podanych parametrach")


                                            #zad 1 "Instrukcja elif"
#
# print("Witaj w kalkulatorze naszego banku!!")
# choose_user = float(input(f"Jeśli chcesz włączyć kalkulator obliczający wartość swojej lokaty w banku wpisz 1 , jeśli kredyt Hipoteczny 2: "))
#
# if choose_user == 1:
#     print("Oblicz z nami wartosc lokaty!")
#
#     value = float(input(" Podaj wartosc w zlotowkach jaka chcesz wplacic na lokate w banku: "))
#     percent = float(input(" Podaj oprocentowanie swojej lokaty: "))
#     years = float(input(" Podaj w latach czas trwania: "))
#
#     interest = (1 + percent/ 100)
#
#     month_user = int(years) * 12
#
#     locate_value = value * interest ** years
#     locate_value_month = value * interest ** (years * 12)
#
#     info = (f"Wartość twojej lokaty po {years} latach, czyli {month_user} miesiacach wynosi: {locate_value:.2f} zł")
#     print(info)
# elif choose_user == 2:
#
#     kredyt_price = float(input("Podaj kwotę kredytu: "))
#     percent_kredyt = float(input("Podaj oprocentowanie kredttu jakie cię interesuje: "))
#     wklad_wlasny = float(input("Podaj wartość wkładu własnego: "))
#     czas_kredytowania = float(input("Podaj czas kredytowania w latach: "))
#     przychod_miesieczny = float(input("Podaj przychód miesięczny: "))
#     suma_miesiecznych_wydatkow = float(input("Podaj sumę swoich miesięcznych wydatków: "))
#
#     rata_kredytu = (kredyt_price * percent_kredyt / 100) / 12 + kredyt_price / (czas_kredytowania * 12)
#     dostepne_srodki = przychod_miesieczny - suma_miesiecznych_wydatkow
#     wartosc_nieruchomosci = wklad_wlasny + kredyt_price
#
#     print(f"Twoja miesięczna rata kredytu dla podanych watości wynosi {rata_kredytu:.2f}")
#     procent_wkladu_do_nieruchomosci = (wklad_wlasny / wartosc_nieruchomosci) * 100
#     print(f"Procentowy udział Twojego wkładu w nieruchomości wynosi: {procent_wkladu_do_nieruchomosci:.2f}%")
#
#     if procent_wkladu_do_nieruchomosci > 20 and dostepne_srodki > (
#             rata_kredytu + 1000) or 10 < procent_wkladu_do_nieruchomosci < 20 and dostepne_srodki > (
#             rata_kredytu + 2000):
#         print(f"Gratulację spełniasz warunki wzięcia kredytu!!")
#     else:
#         print(f"Twój wkład wałsny jest za niski aby wziąć kredyt o podanych parametrach")
# else:
#     print("Niestety wybrałeś/aś nie istniejącą opcję")

                                            #zad 1 "Instrukcja elif"

# print("Witaj w implementacji wyniku testu Coopera!")
#
# wiek = float(input(f"Podaj wiek: "))
# plec = input(f"Podaj swoją płeć (M/K): ")
# uzyskany_wynik = float(input(f"Podaj uzyskany wynik: "))
#
# if 13 <= wiek <= 14:
#     if plec == 'M':
#         if uzyskany_wynik > 2700:
#             print("Bardzo dobrze")
#         elif 2400 <= uzyskany_wynik <= 2700:
#             print("Dobrze")
#         elif 2200 <= uzyskany_wynik <= 2399:
#             print("Średnio")
#         elif 2100 <= uzyskany_wynik <= 2199:
#             print("Żle")
#         else:
#             print("Bardzo źle")
#     elif plec == 'K':
#         if uzyskany_wynik > 2000:
#             print("Bardzo dobrze")
#         elif 1900 <= uzyskany_wynik <= 2000:
#             print("Dobrze")
#         elif 1600 <= uzyskany_wynik <= 1899:
#             print("Średnio")
#         elif 1500 <= uzyskany_wynik <= 1599:
#             print("Żle")
#         else:
#             print("Bardzo źle")
# elif 15 <= wiek <= 16:
#     if plec == 'M':
#         if uzyskany_wynik > 2800:
#             print("Bardzo dobrze")
#         elif 2500 <= uzyskany_wynik <= 2800:
#             print("Dobrze")
#         elif 2300 <= uzyskany_wynik <= 2499:
#             print("Średnio")
#         elif 2200 <= uzyskany_wynik <= 2299:
#             print("Żle")
#         else:
#             print("Bardzo źle")
#     elif plec == 'K':
#         if uzyskany_wynik > 2100:
#             print("Bardzo dobrze")
#         elif 2000 <= uzyskany_wynik <= 2100:
#             print("Dobrze")
#         elif 1700 <= uzyskany_wynik <= 1999:
#             print("Średnio")
#         elif 1400 <= uzyskany_wynik <= 1699:
#             print("Żle")
#         else:
#             print("Bardzo źle")
# elif 17 <= wiek <= 20:
#     if plec == 'M':
#         if uzyskany_wynik > 3000:
#             print("Bardzo dobrze")
#         elif 2700 <= uzyskany_wynik <= 3000:
#             print("Dobrze")
#         elif 2500 <= uzyskany_wynik <= 2699:
#             print("Średnio")
#         elif 2300 <= uzyskany_wynik <= 2499:
#             print("Żle")
#         else:
#             print("Bardzo źle")
#     elif plec == 'K':
#         if uzyskany_wynik > 2300:
#             print("Bardzo dobrze")
#         elif 2100 <= uzyskany_wynik <= 2300:
#             print("Dobrze")
#         elif 1800 <= uzyskany_wynik <= 2099:
#             print("Średnio")
#         elif 1600 <= uzyskany_wynik <= 1799:
#             print("Żle")
#         else:
#             print("Bardzo źle")
# else:
#     print("Podałeś błędny wybór")

                                                # zad 1 " Operatory in oraz is"
# favorite_meals = []
#
# first_meals = input("Podaj nazwę swojej ulubionej potrawy: ")
# favorite_meals.append(first_meals)
# second_meals = input("Podaj nazwę swojej drugiej ulubionej potrawy: ")
# favorite_meals.append(second_meals)
# third_meals = input("Podaj nazwę swojej trzeciej ulubionej potrawy: ")
# favorite_meals.append(third_meals)
#
#
# print("Twoje ulubione potrawy w kolejności to: ", favorite_meals)
#
# if "Zupa" in favorite_meals:
#     print("Wow lubisz Zupę !!!")

                                                # zad 2 " Operatory in oraz is"



# user_phon_number = input("Podaj swój numer telefonu: ")
# user_phon_number = user_phon_number.replace(' ', '')
# user_phon_number = user_phon_number.replace('-', '')
#
# if "0" in user_phon_number:
#     print("W twoim numerze telefonu znajduje się 0 xD")
#
# show_digits = user_phon_number[:6]
# shadow_digits = len(user_phon_number) - 6
# private_digits = "-" * shadow_digits
# anonymous_number = show_digits + private_digits
# print(f"Zanonimizowany numer ktory podales to: ",anonymous_number)

