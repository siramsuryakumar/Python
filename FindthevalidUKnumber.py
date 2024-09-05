# Find the valid UK number

import re

str_variable = input().strip()

def check_valid_phonenumber(str_variable):
    tra_variable = re.sub(r'[^0-9+\s]', '', str_variable)
    if str_variable.startswith('+44') and tra_variable == str_variable:
        print(len(str_variable))
        if len(str_variable) == 12 or 13:
            return str_variable + ' is Valid UK Number'
        else:
            return str_variable + ' is Invalid UK Number'
    else:
        return str_variable + ' is Invalid UK Number'

print(check_valid_phonenumber(str_variable))
