student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores.items():
    if student_scores[student] <= 70:
        student_grades[student] = "Fail"
    elif student_scores[student] > 70 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] > 80 and student_scores[student] <= 90:
        student_grades[student] = "Exceeds Expectations"
    else:
        student_grades[student] = "Outstanding"

# 🚨 Don't change the code below 👇
print(student_grades)
