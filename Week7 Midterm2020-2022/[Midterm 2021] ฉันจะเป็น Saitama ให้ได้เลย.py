'''[Midterm 2021] ฉันจะเป็น Saitama ให้ได้เลย'''
import math

def saitama():
    '''Saitama Function'''
    push = int(input())
    situp = int(input())
    sitdown = int(input())
    run = int(input())
    timepush = int(input())
    timeup = int(input())
    timerun = int(input())
    timedown = int(input())
    daypush = math.ceil(push/timepush)
    daysitup = math.ceil(situp/timeup)
    daysitdown = math.ceil(sitdown/timedown)
    dayrun = math.ceil(run/timerun)
    themost = daypush
    if themost < daysitup:
        themost = daysitup
    if themost < daysitdown:
        themost = daysitdown
    if themost < dayrun:
        themost = dayrun
    print(themost)

saitama()
