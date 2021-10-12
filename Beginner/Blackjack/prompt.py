from getpass import getpass


def prompt_input(question, callback, *args, secret=False):
    """Custom prompt function used to validate user input.\nAny number of parameters are optional for callback flexibility.\nUse parameter keyword 'secret = True' syntax for masking user input."""
    isValid = False
    response = ""
    while(not isValid or response == ""):
        if secret == True:
            response = getpass(question)
        else:
            response = input(question)
        isValid = callback(response, *args)
    return response