from validation import auto_valid, element_in, is_number
from prompt import prompt_input

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


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
        new_position = position - shift
        plain_text += alphabet[new_position]
    print(f"Encoded text: {plain_text}")


run = True
while run:
    direction = prompt_input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n", element_in, ['encode', 'decode'])
    text = prompt_input("Type your message:\n", auto_valid).lower()
    shift = int(prompt_input("Type the shift number:\n", is_number))
    if direction == "encode":
        encrypt(text, shift)
    else:
        decrypt(text, shift)
    run = True if prompt_input("Exit? y/n", element_in, ['y', 'n']) == 'n' else False
