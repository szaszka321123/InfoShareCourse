import math

lenght_first = float(input(f"Podaj długość pierwszej przyprostokątnej: "))
lenght_second = float(input(f"Podaj długość drugiej przyprostokątnej: "))

c = math.sqrt(pow(lenght_first, 2) + pow(lenght_second, 2))

print(f"Długośc przyprostokątnej na podstawie przeciwprostokątych {lenght_first} oraz {lenght_second} wynosi: {c:.2f}")
