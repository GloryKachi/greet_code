# if __name__ == '__main__':
# arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]

# for i in range(1, 11):
# if i not in arr:
# print(i)
def missing_value(values):
    for i in range(1, len(values)):
        print(values)


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    for i in range(1, 11):
        if i not in arr:
            print(i)
