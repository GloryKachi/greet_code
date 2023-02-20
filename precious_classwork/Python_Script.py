"""
1. Write a Python script to generate and print a dictionary that contains a number
(between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""
if __name__ == '__main__':
    values = {}
    number = int(input("Enter number: "))

    for item in range(1, number + 1):
        values[item] = item * item
        # print(f"{item}: {values[item]}")
    print(values)