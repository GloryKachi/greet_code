if __name__ == '__main__':
    index = [4, 9, 12, 13, 2, 1, 0]
    rangeNumber = 3
    listOfSum = []

    for i in range(len(index) - rangeNumber + 1):
        summation = 0
        for j in range(i, rangeNumber + i):
            summation = summation + index[j]
        listOfSum.append(summation)
    print(max(listOfSum))
