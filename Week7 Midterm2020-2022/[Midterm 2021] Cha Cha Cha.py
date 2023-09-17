'''[Recommend + Midterm 2021] Cha Cha Cha'''
import math
def salary(day):
    '''Salary Function'''
    total = 0
    for _ in range(day):
        hours = float(input())
        total += math.ceil(hours)
    total *= 8720
    print(total)

salary(int(input()))
