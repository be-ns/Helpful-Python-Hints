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
