from exercises.exerc_2 import named_arguments

def run_example():

    first_dict = {
        "Imię": "Daniel",
        "Nazwisko": "Kowslaski",
        "Wiek": "26",
        "Wzrost": "187"
    }

    second_dict = {
        "Imię": "Agata",
        "Nazwisko": "Kowslaski",
        "Wiek": "27",
        "Wzrost": "172"
    }

    third_dict = {
        "Imię": "Other",
        "Nazwisko": "Kowslaski",
        "Wiek": "25",
        "Wzrost": "150"
    }

    new_dict = {**first_dict, **second_dict, **third_dict}
    print(new_dict)
    named_arguments(**new_dict)

if __name__ == "__main__":
    run_example()