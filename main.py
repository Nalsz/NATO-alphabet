import pandas

#TODO 1. Create a dictionary in this format:
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(new_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
nato_word = input("Enter a word: ").upper()
nato_output = [new_dict[letter] for letter in nato_word]
print(nato_output)

