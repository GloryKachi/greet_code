import random

if __name__ == '__main__':

    number = random.randint(1, 10)
    # x = 3
    # for y in range(x):
    x = 0
    while x != 3:
        guess = int(input("Guess a number between 1 and 10: "))
        x += 1
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        elif guess == number:
            print("You win!")
