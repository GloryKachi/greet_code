if __name__ == '__main__':

    numbers = [2, 3, 4, 5, 6, 7, 8, ]
    range_number = 3
    list_of_sum = []

    for i in range(len(numbers) - range_number + 1):
        summation = 0
        for j in range(i, range_number + 1):
            summation = summation + numbers[j]
        list_of_sum.append(summation)
    print(max(list_of_sum))


