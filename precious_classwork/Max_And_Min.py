if __name__ == '__main__':

    maximum_number = 0
    minimum_number = 0
    for user_input in range(0, 100):
        user_input = int(input("Enter five numbers: "))
        if user_input == maximum_number :
            maximum_number = user_input
        elif user_input < minimum_number:
            minimum_number = user_input

    print(f"The highest score is {maximum_number}")
    print(f"The minimum number is {minimum_number}")
