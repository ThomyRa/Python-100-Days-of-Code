import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_df = pd.DataFrame(student_dict)
print(student_df)

# Looping trough Rows in Data Frames
for (idx, row) in student_df.iterrows():
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
