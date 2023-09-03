'''[Midterm 2023] Longer'''
import math as m

def longer(raduis, numa, numb):
    '''circle or rectangle'''
    circle = 2 * m.pi * raduis
    rectangle = (numa*2) + (numb*2)
    if circle > rectangle:
        print("Circle is longer\n{:.5f}".format(circle - rectangle))
    elif rectangle > circle:
        print("Rectangle is longer\n{:.5f}".format(rectangle - circle))
    else:
        print("Equal\n{:.5f}".format(circle - rectangle))

longer(float(input()), float(input()), float(input()))
