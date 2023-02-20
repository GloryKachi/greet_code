if __name__ == '__main__':
    print("This is Glory's love calculator")
    user_input = input("Enter your name to see if you're compatible with your partner\n")
    user_input2 = input("Enter your partners name again\n")

    combined_input = user_input + user_input2
    upper_case = combined_input.upper()

    T = upper_case.count("T")
    R = upper_case.count("R")
    U = upper_case.count("U")
    E = upper_case.count("E")

    true_combination = T + R + U + E

    L = upper_case.count("L")
    O = upper_case.count("O")
    V = upper_case.count("V")
    E = upper_case.count("E")

    love_combination = L + O + V + E
    compatibility_check = int(str(true_combination) + str(love_combination))

    if compatibility_check < 10 or compatibility_check > 90:
        print(f"Your love score is {compatibility_check} you go like coke and mentos")
    elif compatibility_check == 40 and compatibility_check == 50:
        print(f"Your love score is {compatibility_check}. You are alright together")
    else:
        print(f"Your love score is {compatibility_check}")
