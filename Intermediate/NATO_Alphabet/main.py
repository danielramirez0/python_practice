import pandas
data = pandas.read_csv("nato_phonetics.csv")

phonetics = {row.letter:row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Type a word: ").upper()
    try:
        phonetic_list = [phonetics[letter] for letter in word]
    except KeyError:
        print("Only letters are allowed")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()