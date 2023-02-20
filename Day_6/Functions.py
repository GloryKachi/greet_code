if __name__ == '__main__':
    user_input1 = int(input("Enter number: "))
    user_input2 = int(input("Enter number: "))
    user_input3 = int(input("Enter number: "))
    user_input4 = int(input("Enter number: "))
    user_input5 = int(input("Enter number: "))
    for numbers in range(user_input1):
        if user_input1 > user_input2 and user_input1 > user_input3 and \
                user_input1 > user_input4 and user_input1 > user_input5:
            print(f"{user_input1} is the maximum number")
        elif user_input2 > user_input1 and user_input2 > user_input3 \
                and user_input2 > user_input4 and user_input2 > user_input5:
            print(f"{user_input2} is the maximum number")
        elif user_input3 > user_input1 and user_input3 > user_input2 and user_input3 > \
                user_input4 and user_input3 > user_input5:
            print(f"{user_input3} is the maximum number")
        elif user_input4 > user_input1 and user_input4 > user_input2 and user_input4 > \
                user_input3 and user_input4 > user_input5:
            print(f"{user_input4} is the maximum number")
