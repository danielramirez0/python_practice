import random
day_of_week = "Monday"
print(day_of_week)
day_of_week = "Friday"
print("I can't wait for " + day_of_week)

# animal_input = input("What is your favorite animal?")
# color_input = input("What is your favorite color?")
# print(f"I've never seen a {color_input} {animal_input}")

time_of_day = 1700
selected_meal = ""
if time_of_day < 1200:
    selected_meal = 'Eggs'
elif time_of_day > 1200 and time_of_day < 1700:
    selected_meal = 'Pizza'
elif time_of_day > 1700:
    selected_meal = 'Chicken'

print(selected_meal)

random_number = random.randrange(0, 10)
if random_number >= 0 and random_number <= 2:
    print("Beatles")
elif random_number >= 3 and random_number <= 5:
    print("Stones")
elif random_number >= 6 and random_number <= 8:
    print("Floyd")
elif random_number == 9 or random_number == 10:
    print("Hendrix")

for number in range(7):
    print("Python is cool")

for number in range(11):
    print(number)

for number in range(5):
    print("hello")
    print("goodbye")

height = 40
while height < 48:
    print('Cannot ride')
    height += 1

# magic_number = random.randrange(0,100)
# guess = 0
magic_number = 50
guess = 50
while guess != magic_number:
    guess = int(input("Guess my number: "))
    difference = magic_number - guess
    difference = abs(difference)
    if guess < magic_number:
        print("Too Low!")
    if guess > magic_number:
        print("Too High!")
    if difference <= 10 and difference != 0:
        print("Getting warmer!")
    if magic_number == guess:
        print("Congradulations!")


def print_movie_name():
    favorite_movie = "The Departed"
    print(favorite_movie)


print_movie_name()


def get_favorite_band():
    # favorite_band = input("What is your favorite band?")
    favorite_band = 'Thrice'
    return favorite_band

band = get_favorite_band()

print(band)


def concert_display(musical_act):
    # my_street = input("Enter your street name: ")
    my_street = "Cool street"
    print(f"It would be great if {musical_act} played a show on {my_street}")


concert_display(band)

desktop_items = ['desk', 'lamp', 'computer']

print(desktop_items[1])

desktop_items.append("Infinity Guantlet")
for item in desktop_items:
    print(item)