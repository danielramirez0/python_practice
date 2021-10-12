from art import logo
from validation import element_in, auto_valid, is_all_letters
from prompt import prompt_input

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, starting_text, cipher_key):
    out_text = ''
    if cipher_key >= len(alphabet):
        cipher_key = cipher_key % len(alphabet)
    if direction == "decode":
        cipher_key *= -1
    for char in starting_text:
        position = alphabet.index(char)
        if position + cipher_key >= len(alphabet):
            new_position = (position + cipher_key) - len(alphabet)
        else:
            new_position = position + cipher_key
        out_text += alphabet[new_position]
    print(f'The text {starting_text} changed to {out_text}')

print(f'{logo}')
run = True
while run:
    direction = prompt_input("Type 'encode' to encrypt, type 'decode' to decrypt:\n", element_in, ['encode', 'decode'])
    text = prompt_input("Type your message:\n", is_all_letters, alphabet).lower()
    shift = int(prompt_input("Type the shift number:\n", auto_valid))
    caesar(direction, text, shift)
    esc = prompt_input("Exit [y/n]: ", element_in, ['y', 'n'])
    run = False if esc == 'y' else True
