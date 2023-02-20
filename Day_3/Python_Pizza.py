if __name__ == '__main__':
    print("Welcome to Python Pizza")
    size = input("Enter S for small, M for medium or L for large\n")
    bill = 0

    if size == "S":
        bill += 15
        print("Small pizza is $15")
    elif size == "M":
        bill += 20
        print("Medium pizza is $20")
    elif size == "L":
        bill += 25
        print("Large pizza is $25")

        pepperoni = input("Would you love some pepperoni? Input Y if you're buying"
                          " a small pizza or YY if you're buying a medium or large pizza")
        if pepperoni == "Y":
            if size == "S":
                bill += 2
        elif pepperoni == "YY":
            pepperoni += 3

            extra_cheese = input("Would you love some extra cheese? Input Y if you'd love an extra cheese")
            if extra_cheese == "Y":
                extra_cheese += 1
            else:
                print(f"Your total bill is ${bill}")
