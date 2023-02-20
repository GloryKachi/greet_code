def sum_up(lst):
    for i in range(0, len(lst)):
        for j in range(1, len(lst)):
            if lst[i] + lst[j]:
                return lst[i], lst[j]


if __name__ == '__main__':
    array = [2, 3, 4, 5, 6, 7, 8, 5]
    print(sum_up(array))
