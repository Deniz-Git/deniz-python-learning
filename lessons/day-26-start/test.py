import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


student_dict_frame = pd.DataFrame(student_dict)

# for (key, value) in student_dict_frame.items():
#     print(value)

for (index, row) in student_dict_frame.iterrows():
    if row.student == "Angela":
        print(row.score)