MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": float(0)
}


def prompt_user():
    return input("What would you like? espresso/latte/cappuccino : ")


def on():
    running = True
    coins = []
    while running:
        response = prompt_user()
        if response == 'off':
            running = False
            break
        if response == 'report':
            print(
                f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
        else:
            drink = MENU[response]
            for key in drink["ingredients"]:
                if drink['ingredients'][key] > resources[key]:
                    print("Not enough resources to make drink")
                    on()
                    running = False
            paying = True
            print(f"Cost = {drink['cost']}")
            while paying:
                coin = input('Insert coin name: ')
                qty = int(input("How many coins? "))
                for i in range(qty):
                    coins.append(coin)
                if input("More? ") != 'y':
                    paying = False
            paid = 0
            for coin in coins:
                if coin == 'quarter':
                    paid += .25
                elif coin == 'dime':
                    paid += .10
                elif coin == 'nickel':
                    paid += .05
                elif coin == 'penny':
                    paid += .01
            if paid < drink["cost"]:
                print(f"Not enough money to make drink, refunded {paid}")
                on()
                running = False
            else:
                if paid > drink['cost']:
                    refund = paid - drink['cost']
                    print(f"Refunded over payment ${refund}")
                resources['money'] += drink['cost']
            for key in drink["ingredients"]:
                resources[key] -= drink["ingredients"][key]
            print(f"Here is your {response}")


on()
