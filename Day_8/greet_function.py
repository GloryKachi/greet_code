import math


def greet():
    print("Good morning")
    print("How was your day?")
    print("See you later")


def greet_with(name, location):
    print(f"Hello {name}\nWhat is it like in {location}?")


def calculate_paint(wall_height, wall_width, coverage):
    area = wall_height * wall_width
    number_of_cans = math.ceil(area / coverage)
    print(f"You'll need {number_of_cans} cans of paint")


def assert_prime_number(number):
    is_prime = True
    for numbers in range(2, number - 1):
        if number % numbers == 0:
            is_prime = False
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is an even number")


if __name__ == '__main__':
    assert_prime_number(7)
    greet_with(location="Yaba", name="Bob")
    height_of_wall = int(input("Enter wall height:\n "))
    width_of_wall = int(input("Enter wall width:\n "))
    wall_coverage = int(input("Enter wall coverage:\n "))
    calculate_paint(wall_height=height_of_wall, wall_width=width_of_wall, coverage=wall_coverage)
