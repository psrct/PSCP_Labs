'''Align'''
def light(size, choose, word):
    '''left center right'''
    if choose == "left":
        print("%s" %word.ljust(size))
    elif choose == "right":
        print("%s" %word.rjust(size))
    elif choose == "center" and (size - len(word)) %2 != 0:
        size -= 1
        print(" " + "%s" %word.center(size))
    else:
        print("%s" %word.center(size))

light(int(input()), input(), input())
