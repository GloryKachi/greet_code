if __name__ == '__main__':
    user_input = input("Type a word: ").upper()
    user_input2 = input("Enter numbers: ")

    list_user_input = list(user_input)
    print(list_user_input)

    list_user_input.sort()
    print(list_user_input)
# =======================================

    list_user_number = list(user_input2)
    print(list_user_number)

    list_user_number.sort()
    number = []
    for element in list_user_number:
        number.append(element)
    print("".join(number))
