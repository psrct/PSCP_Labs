'''LastStand'''
import json

def last(text):
    '''Last Function'''
    textlist = json.loads(text)
    for i in textlist:
        count = len(str(i))
        print(str(i)[count - 1])

last(input())
