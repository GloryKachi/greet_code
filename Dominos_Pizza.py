def dominos_pizza(expected_amount, current_amount, available_balance):
    offender_fee = (expected_amount - current_amount) // available_balance
    return int(offender_fee)


if __name__ == '__main__':
    pizza_amount = int(input("Enter pizza amount\n"))
    available_amount = int(input("Enter available amount\n"))
    offenders_fee = int(input("Enter offenders fee\n"))
    print(f"{dominos_pizza(pizza_amount, available_amount, offenders_fee)} offenders will pay")
 