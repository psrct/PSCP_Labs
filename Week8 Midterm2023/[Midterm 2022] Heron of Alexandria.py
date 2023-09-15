'''[Midterm 2022] Heron of Alexandria'''
import math
def area(numa, numb, numc):
    '''Area'''
    nums = (numa + numb + numc)/2
    areas = math.sqrt((((nums * (nums-numa)) * (nums - numb)) * (nums - numc)))
    print("%.3f" %areas)
area(float(input()), float(input()), float(input()))
