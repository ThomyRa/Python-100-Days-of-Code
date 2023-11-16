import random
from prettyprinter import pprint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}
pprint(student_scores)

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
pprint(passed_students)
