'''Inverter'''

def invert(text):
    '''Inverter Function'''
    word = ""
    for i in text:
        word += check(i)
    print(word.lstrip("0"))

def check(index):
    '''Check Function'''
    if index == "0":
        return "1"
    else:
        return "0"

invert(input())
