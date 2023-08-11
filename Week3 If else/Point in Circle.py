'''Point in Circle'''
import math as m
def main(numx, numy, radius, num_xn, num_yn):
    '''distance = x2-x1 **2'''
    if radius >= distance(numx, numy, num_xn, num_yn):
        print("True")
    else:
        print("False")
def distance(numx, numy, num_xn, num_yn):
    '''distance = ?'''
    dist = m.sqrt(((num_xn - numx)**2) + ((num_yn - numy)**2))
    return dist
main(float(input()), float(input()), float(input()), float(input()), float(input()))
