import random

if __name__ == '__main__':
    today_date = int(input("Enter today's day: "))
    future_day = int(input("Enter the number of days elapsed since today: "))
    random_value = today_date + future_day

    weeks = random.randint(0, 6)
    if weeks == 0 and future_day == 0:
        print("Today is Sunday")

        if weeks == 1:
            print(f"Today is Monday and future day is {future_day}")
            if weeks == 2 and future_day == 2:
                print("Today is Tuesday")
                if weeks == 3 and future_day == 3:
                    print("Today is Wednesday")
