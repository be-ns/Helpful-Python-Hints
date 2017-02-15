# helpful python bits to reuse and save time
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# this clears screen while running scripts to debug in clean clear way

zfill()
# builtin function that pads leftside of string with 0 unless it is the required amount of characters
# so if hi = 'hi'
hi.zfill(3) would return '0hi'


# `operator` library
# This class turns the standard mathematical calculations you write, `+` and `-`, into functions, `sum()` and `sub()`, respectively.
# These functions can make your life easier as you're trying to implement your program.
# This can also allow for more complicated operations (`sin`, `tan`, `cos`, and `pi`).
