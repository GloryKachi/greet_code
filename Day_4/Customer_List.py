if __name__ == '__main__':
    import random

    toss_coin = int(input("Create a seed number: \n"))
    random.seed(toss_coin)

    customer_names = input("Enter names of participants\n").upper()
    names = customer_names.split(",")
    total_number_of_names = len(names)
    shuffled_names = random.randint(0, total_number_of_names - 1)
    bill_handler = names[shuffled_names]
    print(bill_handler + " is going to pay the bill")
