def check_prime_number(number):
    is_prime = True
    for num in range(2, number-1):
        if number % num == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")


if __name__ == '__main__':
    user_input = int(input("Enter number: "))
    check_prime_number(number=user_input)

