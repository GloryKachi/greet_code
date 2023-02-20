import random

if __name__ == '__main__':
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z",
               "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
               "V", "X", "Y", "Z"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "@", "#", "%", "^", "&", "*", "(", ")", "-", "*", "+"]

    print("Generate a strong password with G-password")

    letters2 = int(input("Enter number of letters: "))
    numbers2 = int(input("Enter numbers: "))
    symbols2 = int(input("How many symbols would you love to add in your password? "))

    user_input = letters2 + numbers2 + symbols2
    random.Random(user_input)

    if letters2 == user_input:
        print(letters in range(user_input))

    print(user_input)
