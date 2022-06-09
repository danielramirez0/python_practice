import pandas
data = pandas.read_csv("nato_phonetics.csv")

phonetics = {row.letter:row.code for (index, row) in data.iterrows()}

while True:
    word = input("Type a word or (q) to exit: ").upper()
    if word == "Q": break
    print([phonetics[letter] for letter in word])

