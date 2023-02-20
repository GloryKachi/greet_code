if __name__ == '__main__':
    import random

    user_input = int(input("Create a seed number: \n"))
    random.seed(user_input)
    random_numbers = random.randint(0, 1)

    if user_input == random_numbers:
        print("Heads!")
    else:
        print("Tails!")
