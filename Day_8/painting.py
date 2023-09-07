import math


def get_num_of_paint(height, width):
    coverage = 5
    total_num_of_paint = height * width / coverage
    return math.floor(total_num_of_paint)


if __name__ == '__main__':
    user_input = int(input("Enter height of wall: "))
    user_input2 = int(input("Enter width of wall: "))

    print(f"You'll get {get_num_of_paint(height=user_input, width=user_input2)} cans of paint")
