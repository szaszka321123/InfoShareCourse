import Calculator.Calculations.fukcja_obliczająca

def user_informations():
    start_up_capital = input(f"Podaj kapitał początkowy we wpłaconej kwocie: ")
    percent = input(f"Podaj oprocentowanieL: ")
    years = input(f"Podaj czas trwania inwestycji w latach: ")
    return start_up_capital, percent, years

capital_start, percent_capital, years_capital = user_informations()

resultat = Calculator.Calculations.fukcja_obliczająca.calculations(first_capital=float(capital_start), percent=float(percent_capital), time=float(years_capital))
print(f"Twoja inwestycja po {years_capital} wyniesie : {resultat:.2f} Zł")
