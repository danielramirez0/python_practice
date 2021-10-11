from getpass import getpass

# Function for prompting for user input, accepts a callback and options to include up to two optional parameters in callback call
def prompt_input(question, callback, opt_param_1=False, opt_param_2=False, secret=False):
    isValid = False
    response = ""
    while(not isValid or response == ""):
        if secret:
            response = getpass(question)
        else:
            response = input(question)
        if opt_param_1 and opt_param_2:
            isValid = callback(response, opt_param_1, opt_param_2)
        elif opt_param_1:
            isValid = callback(response, opt_param_1)
        else:
            isValid = callback(response)
    return response
