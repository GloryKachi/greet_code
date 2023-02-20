if __name__ == '__main__':
    firstNumber = int(input("Enter first number: "))
    secondNumber = int(input("Enter second number: "))

    square1 = firstNumber * firstNumber
    square2 = secondNumber * secondNumber
    sumOfSquare = square1 + square2
    differenceOfSquares = square1 - square2

    print(f"Your first input is {firstNumber}\nYour second input is {secondNumber}\n"
          f"The square of {firstNumber} is {square1}\nThe square of {secondNumber} is {square2}\n"
          f"The sum of their squares is {sumOfSquare}\nThe difference of their squares is {differenceOfSquares}")
