if __name__ == '__main__':

    weight = float(input("Enter your weight: "))
    height = float(input("Enter your height: "))

    bodyMassIndex = weight * 703 / (height * height)
    print(f"Your BMI is {bodyMassIndex}")

    if bodyMassIndex < 18.5:
        print("You are underweight. You may need to put on some weight!")
    elif bodyMassIndex >= 18.5:
        print("You are at a healthy weight for your height\n" +
              "Congratulations! you lower your risk of developing serious health problems")
    elif bodyMassIndex == 29.9:
        print("You are slightly overweight!\n" +
              "You may need to lose some weight for health reasons")
    elif bodyMassIndex > 29.9:
        print("You are heavily overweight!\n" +
              "Your health may be at risk if you do not lose weight")
