if __name__ == '__main__':
    weight = float(input("Enter weight in Kilogram:\n"))
    height = float(input("Enter height in inches:\n"))
    bmi = round(weight / (height ** 2), 2)
    # total = round(bmi, 2)
    print(f"Your BMI is {bmi}")

    if bmi <= 18.5:
        print("You are under weight!\n")
    elif bmi > 18.5 or bmi == 24:
        print("You have a normal weight\n")
    elif bmi > 24 or bmi == 29:
        print("You are over weight!\n")
    elif bmi > 29 or bmi == 34:
        print("You are obese!\n")
    else:
        print("You are clinically obese!\n")
