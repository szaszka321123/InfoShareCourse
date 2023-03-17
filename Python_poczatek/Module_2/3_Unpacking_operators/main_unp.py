from exercises.exerc_2 import named_arguments

def run_example():

    new = named_arguments(
        Imię = "Daniel",
        Nazwisko = "Iwanowski",
        Wiek = 26,
        Wzrost = 187
    )
    print(new)


if __name__ == "__main__":
    run_example()