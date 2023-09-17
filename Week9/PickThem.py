'''PickThem'''
import json

def convert(text):
    '''Convert Function'''
    lit1 = []
    lis = json.loads(text)
    for i in lis:
        if i % 2 == 0:
            lit1.append(i)
    if lit1 == []:
        print("Nope")
    else:
        for i in lit1:
            print(i)

convert(input())
