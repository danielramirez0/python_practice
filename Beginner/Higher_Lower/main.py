from random import choices
from game_data import data as DATA
from art import logo as LOGO, vs as VS
from os import system

CLEAR = lambda:system('clear')

def display(option):
    print(f"{option}")

def get_random_options():
    return choices(DATA, k=2)

display(LOGO)
display(VS)
print(f'{get_random_options()}')
CLEAR()

