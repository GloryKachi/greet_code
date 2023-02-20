if __name__ == '__main__':
    students_grade = int(input("Enter students grade: "))
    # students_grade = (students_grade)
    highest_number = 0
    for grades in students_grade:
        if grades > highest_number:
            highest_number = grades

print(f"The highest score is {highest_number}")
