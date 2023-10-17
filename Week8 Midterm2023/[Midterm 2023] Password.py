'''Password'''
import math
def passwords(text):
    '''Password Functions'''
    haslow = 0
    hasupper = 0
    hasnum = 0
    haskey = 0
    longtext = len(text)
    for i in text:
        if i.islower():
            haslow = 26
        elif i.isupper():
            hasupper = 26
        elif i.isdigit():
            hasnum = 10
        else:
            haskey = 32
    pool = haslow + hasupper + haskey + hasnum
    pool = (math.floor(math.log2(pool**longtext)))
    print(pool)
    if 28 > pool:
        print("Very Weak")
    elif 28 <= pool <= 35:
        print("Weak")
    elif 36 <= pool <= 59:
        print("Reasonable")
    elif 60 <= pool <= 127:
        print("Strong")
    else:
        print("Very Strong")
passwords(input())
