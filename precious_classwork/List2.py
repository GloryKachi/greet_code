if __name__ == '__main__':
    list_1 = [1, 2, 3, 4, 5]
    list_2 = ['a', 'b', 'c', 'd', 'e']

    dictionary = {}
    value = 0
    for item in list_1:
        dictionary[item] = list_2[value]
        value += 1
    print(dictionary)


