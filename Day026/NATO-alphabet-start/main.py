import pandas as pd

nato_alphabet_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_dict = {row.letter: row.code for (idx, row) in nato_alphabet_df.iterrows()}

user_word = input("Insert a word: ")
letters = list(user_word)
upper_letters = [letter.upper() for letter in letters]
phonetic_list = [nato_alphabet_dict[letter] for letter in upper_letters]
print(phonetic_list)
