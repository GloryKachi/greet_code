students_scores = {
    "Thomas": 81,
    "Peter": 78,
    "James": 99,
    "John": 74,
    "Matthew": 62,
}

students_grades = {}

for key in students_scores:
    value = students_scores[key]
    if value > 90:
        students_grades[key] = {"Outstanding"}
    elif value > 80:
        students_grades[key] = {"Exceeds expectations"}
    elif value > 70:
        students_grades[key] = {"Acceptable"}
    else:
        students_grades[key] = {"Fail"}
# print(students_grades)


