if __name__ == '__main__':

    print("Enter the number of times to calculate citizens tax rate: ");
    userInput = int(input())
    firstCitizenTax = 0
    secondCitizenTax = 0
    thirdCitizenTax = 0
    inputCounter = 0
    taxRate = 30_000
    combinedTax = 4_500 + 0.2
    result = 0

    while inputCounter < userInput:
        print("Enter first citizen's earnings: ")
        firstCitizen = int(input())
        firstCitizenTax += firstCitizen

        print("Enter second citizen's earnings: ")
        secondCitizen = (input())
        secondCitizenTax += secondCitizen

        print("Enter third citizen's earnings: ")
        thirdCitizen = int(input())
        thirdCitizenTax += thirdCitizen
        inputCounter = inputCounter + 1

    if firstCitizenTax >= taxRate or secondCitizenTax >= taxRate or thirdCitizenTax >= taxRate:
        firstCitizenTax -= combinedTax
        secondCitizenTax -= combinedTax
        thirdCitizenTax -= combinedTax

    elif firstCitizenTax * 0.2:
        firstCitizenTax -= result

    result2 = secondCitizenTax * 0.2
    secondCitizenTax -= result2

    result3 = thirdCitizenTax * 0.2
    thirdCitizenTax -= result3

    # print(f"The first citizen's total tax is %.2f%nThe second citizen's total tax is" +
    #                   " %.2f%nThe third citizen's tax is %.2f" {firstCitizenTax}, {secondCitizenTax}, {thirdCitizenTax}
    #
