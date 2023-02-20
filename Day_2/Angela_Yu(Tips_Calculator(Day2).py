if __name__ == '__main__':
    print("Welcome to tip calculator")
    total_bill = float(input("Enter total bill\n$"))
    percentage_tip = float(input("Enter percentage tip you would like to give\n"))
    spilt_bill = int(input("Enter how many people to spilt the bill\n"))

    final_bill = percentage_tip / 100 * total_bill
    bill = total_bill + final_bill
    bill_per_person = bill / spilt_bill
    final_amount = round(bill_per_person, 2)

    print(f"Each person should pay ${final_amount}")
