if __name__ == '__main__':
    river = 'Mississippi'
    target = input('Input a character to find: ')
    print()
    for index in range(len(river)):
        if river[index] == target:
            print(target, "found at index", index)

            break

    else:
        print("letter", target, "not found in", river)
        print()

    name = "Glory Kachi  MyJulie"
    first, second, third = name.split()
    print("Simi's julie is",first)




