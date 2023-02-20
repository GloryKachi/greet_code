if __name__ == '__main__':
    age = int(input("Enter your age\n"))
    age = 100 - age

    remaining_days = age * 365
    remaining_weeks = age * 52
    remaining_months = age * 12

    print(f"You have {remaining_days} days\n{remaining_weeks} weeks\n{remaining_months} months to live\n"
          f"Please make good use of your life now before you die!")
