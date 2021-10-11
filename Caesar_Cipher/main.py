
from validation import auto_valid, element_in, number_between, is_all_letters
from prompt import prompt_input

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, starting_text, cipher_key):
    if direction == "encode":
        encrypt(starting_text, cipher_key)
    else:
        decrypt(starting_text, cipher_key)


def encrypt(plain_text, cipher_key):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if position + cipher_key >= len(alphabet):
            new_position = (position + cipher_key) - len(alphabet)
        else:
            new_position = position + cipher_key
        cipher_text += alphabet[new_position]
    print(f"Encoded text: {cipher_text}")


def decrypt(cipher_text, cipher_key):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - cipher_key
        plain_text += alphabet[new_position]
    print(f"Decoded text: {plain_text}")


run = True
while run:
    direction = prompt_input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n", element_in, ['encode', 'decode'])
    text = prompt_input("Type your message:\n",
                        is_all_letters, alphabet).lower()
    shift = int(prompt_input("Type the shift number:\n",
                number_between, 1, len(alphabet)))
    caesar(direction, text, shift)
    esc = prompt_input("Exit [y/n]: ", element_in, ['y', 'n'])
    run = False if esc == 'y' else True
