'''Right Arrow'''
import math as m

def rarrow(width, height):
    '''Right Arrow Function'''
    middle = m.floor(height/2)
    for i in range(middle+1):
        print(" " * i + ("*" * width))
    for j in range(middle, 0, -1):
        print(" " * (j-1) + ("*" * width))

rarrow(int(input()), int(input()))
