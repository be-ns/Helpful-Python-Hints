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


# fixing plots in matplotlib where whitespace is bad
def fix_whitespace(ax,buff=0.01):
    """use x and y to add well spaced margins"""
xmin,xmax = ax.get_xlim()
ymin,ymax = ax.get_ylim()
xbuff = buff * (xmax - xmin)
ybuff = buff * (ymax - ymin)
ax.set_xlim(xmin-xbuff,xmax+xbuff)
ax.set_ylim(ymin-ybuff,ymax+ybuff)
