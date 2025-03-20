import pandas as pd   
data_frame = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phonetic_alphabets = {row.letter: row.code for (index, row) in data_frame.iterrows()}
# print(nato_phonetic_alphabets)

word = input("Enter a word: ").upper()
output_list = [nato_phonetic_alphabets[letter] for letter in word]
print(output_list)

