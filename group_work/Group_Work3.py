def sum_array(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i][i]
    return total


if __name__ == '__main__':
    array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(sum_array(array))


def largest(arr):
    largest = 0
    second_largest = 0
    for number in arr:
        if number > largest:
            second_largest = largest
            largest = number

        if second_largest < number < largest:
            second_largest = number

    return largest, second_largest


if __name__ == '__main__':
    lst = [1, 3, 5, 8, 9, 2, 4, 55, 33]
    print(largest(lst))
