if __name__ == '__main__':
    # print("Hello there! Welcome to leap year calculator app!")
    # year = int(input("Enter year\n"))

    # if year % 4 == 0:
    # print(f"{year} is a leap year ")
    # elif year % 400 == 0:
    # print(f"{year} is a leap year")
    # else:
    # print(f"{year} is not a leap year")

    year = int(input("Enter year:\n"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

    