names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
import random
 
student_scores = {student:random.randint(1, 100) for student in names}

passed_students = {student for student in student_scores if student_scores[student] > 60}
pazzed_students = {student:score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)
print(pazzed_students)

for (key, value) in student_scores.items():
    print(key)