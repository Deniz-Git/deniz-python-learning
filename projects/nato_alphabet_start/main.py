# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

df = pd.read_csv("/home/deniz/deniz-python-learning/projects/nato_alphabet_start/nato_phonetic_alphabet.csv")

nato_dict={}
for (index, row) in df.iterrows():
    nato_dict[row.letter] = row.code


power_on = True
while power_on:
    user_input = str(input("Please input your name to be coded: ").upper())
    if user_input == "EXIT":
        print("Shutting off...")
        power_on = False
    else:
        try:
            result = [nato_dict[letter] for letter in user_input]
        except KeyError:
            print("Sorry, only letters in the alphabet please.")
        else:
            print(result)
        
