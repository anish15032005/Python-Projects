student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Loop through dictionaries
# for (key,value) in student_dict.items():
#     # print(value)
    
#looping through pandas
import pandas as pd   
student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# for (key, value) in student_data_frame.items():
#     # print(value)
#     print(value)

for (index,row) in student_data_frame.iterrows():
    # print(index)
    print(row.student)
    print(row.score)