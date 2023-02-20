if __name__ == '__main__':

    user_input = int(input("Enter students height:\n"))
    students_height = [user_input]
    total = 0
    for heights in students_height:
        total += heights
        final_result = (total / heights)
        total = round(final_result)
print(total)

