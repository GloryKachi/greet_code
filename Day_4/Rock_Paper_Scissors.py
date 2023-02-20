import random

if __name__ == '__main__':
    user_input = int(input("Enter 0 for rock, 1 for paper and 2 for scissors:\n"))
    computer_choice = random.randint(0, 2)
    print(f"The computer chose {computer_choice}")

    if user_input == 2 and computer_choice == 1:
        print("You win!")
    elif computer_choice == 2 and user_input == 1:
        print("You  loose")
    elif user_input == 1 and computer_choice == 0:
        print("You win!")
    elif computer_choice == 1 and user_input == 0:
        print("You loose")
    elif user_input == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_input == 2:
        print("You loose")
    elif computer_choice == user_input:
        print("It's a draw")
    elif user_input > 2 or user_input < 0:
        print("You entered an invalid number")

