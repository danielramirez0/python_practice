
def number_in(n, arr):
    try:
        int(n)
    except:
        print('Only numbers are accepted')
        return False
    if int(n) in arr:
        return True
    else:
        print(f"Selection must be one of the following:")
        for number in arr:
            print(f"{number}")
        return False


def number_between(n, a, b):
    try:
        int(n)
    except:
        print('Only numbers are accepted')
        return False
    if int(n) >= a and int(n) <= b:
        return True
    else:
        print(f"Selection must be between {a} and {b}")
        return False


def element_in(element, arr):
    if (element) in arr:
        return True
    else:
        print("Not a valid option, try again")
        return False

def is_all_letters(str, arr):
    for letter in str:
        if letter in arr:
            continue
        else:
            print(f"{letter} is not a letter")
            return False
    return True


def auto_valid(a):
    return a == a


def is_odd(num1):
    try:
        int(num1)
    except:
        print('Only enter numbers')
        return False
    if int(num1) % 2 != 0:
        return True
    else:
        print(f'Number must be an odd number')
        return False


def is_number(num):
    try:
        int(num)
    except:
        print('Only enter numbers')
        return False
    return True
