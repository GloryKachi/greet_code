if __name__ == '__main__':
    numbers = 0
    for numbers in range(1, 100):

        if numbers % 3 == 0:
            print("buzz!")
        elif numbers % 5 == 0:
            print("fizz!")
        elif numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz!")
        else:
            print(numbers)
