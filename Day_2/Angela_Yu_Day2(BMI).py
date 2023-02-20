if __name__ == '__main__':
    height = input("Enter your height in meters\n")
    weight = input("Enter your weight in kilogram\n")
    bmi = int(weight) / float(height) ** 2
    print(int(bmi))
