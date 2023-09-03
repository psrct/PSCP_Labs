'''[Midterm 2023] Niwarn World'''
import math as m

def niwarn(numn, nums, numk):
    '''[Midterm 2023] Niwarn World'''
    varz = ((y_ns(numk, numk))**2 + ((8456 * (x_n(numk))**4)/(24 * numk)))
    print("X: {:.1f}, Y: {:.1f}, Z: {:.1f}".format(x_n(numn), y_ns(numn, nums), varz))
def x_n(num1):
    '''x(n)'''
    varx = 2 + ((m.log2(num1**2))/((2*num1)* (m.log2(num1))))
    return varx

def y_ns(num1, num2):
    '''y(n,s)'''
    return ((m.sin(m.radians(30))) + (m.sqrt(2*num2)))/(x_n(num1)+3)

niwarn(float(input()), float(input()), float(input()))
