if __name__ == '__main__':
    import random

    toss_coin = int(input("Enter a number to toss your coin: \n"))
    random.seed(toss_coin)
    random_side = random.randint(0, 1)

    if toss_coin == 1:
        print("Heads")
    else:
        print("Tails")
