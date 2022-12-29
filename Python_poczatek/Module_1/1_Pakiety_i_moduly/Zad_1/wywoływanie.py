
import Srednia_predkosc_biegu





distance = float(input(f"Podaj dystans jaki przebiegłeś: "))
time = float(input(f"Podja czas w godzinach: "))


speed = Srednia_predkosc_biegu.average_speed(distance=distance, time=time)

print(speed)
