'''Divide3Or5'''
import math

def calculate(number):
    ''' %3 and %5'''
    total = 0
    number = math.floor(number)
    for i in range(1, number+1):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    print(total)
calculate(float(input()))
