from ast import arg


# args is turple
def add(*args):
    sum = 0
    print(args[0])
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4))


# kwargs is dictionary
def calculate(n, **kwargs):
    # for key, value in kwargs.items():
        # print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    '''Example model using kwargs'''

    def __str__(self) -> str:
        return f"{self.make} {self.model} {self.color} {self.seats}"
    
    def __init__(self, **kw) -> None:
        self.make = kw["make"] # will error if make not provided, use get() instead
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

dream_car = Car(make="Nissan", model="GT-R")
print(dream_car)

my_car = Car(make="Subaru", model="Legacy", color="Green", seats="4")
print(my_car)