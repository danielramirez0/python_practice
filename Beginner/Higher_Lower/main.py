from random import choices
from game_data import data as DATA
from art import logo as LOGO, vs as VS
from os import system


def CLEAR(): return system('clear')


def display(option):
    print(option)


def get_random_options():
    return choices(DATA, k=2)

def run():
    correct = False
    incorrect = False
    score = 0
    while not incorrect:
        CLEAR()
        alert = f"You're right! Current score: {score}"
        arr = get_random_options()
        person1 = arr[0]
        person2 = arr[1]
        a = f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']} "
        b = f"Compare A: {person2['name']}, a {person2['description']}, from {person2['country']} "
        display(LOGO)
        if correct:
            print(f"{alert}")
        display(a)
        display(VS)
        display(b)
        answer = input("Who has more followers? Type  A or B : ")
        if answer == 'a' or answer == "A":
            if person1['follower_count'] > person2['follower_count']:
                score += 1
                correct = True
            else:
                alert = f"Sorry, that's wrong. Final score: {score}"
                incorrect = True
        else:
            if person1['follower_count'] < person2['follower_count']:
                score += 1
                correct = True
            else:
                alert = f"Sorry, that's wrong. Final score: {score}"
                incorrect = True
    CLEAR()
    display(LOGO)
    display(alert)
    input()

while True:
    run()