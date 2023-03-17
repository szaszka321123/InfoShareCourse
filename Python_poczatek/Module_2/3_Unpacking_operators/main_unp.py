from exercises.exerc_2 import named_arguments

def run_example():

    frist_list = [1, 2, 3, 4, 5, 6]
    second_list = [7, 8, 9, 10, 11]

    new_list = [*frist_list, *second_list]
    print(new_list)

if __name__ == "__main__":
    run_example()