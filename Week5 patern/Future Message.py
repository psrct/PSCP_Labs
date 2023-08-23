'''Future Message'''

def findtype(word):
    '''Future Message'''
    if word.isdecimal():
        print("Number")
    elif word.isupper():
        print("Uppercase")
    elif word.islower():
        print("Lowercase")
    elif word.istitle():
        print("Title")
    elif word.isspace():
        print("Space")
    else:
        print("Other")

findtype(input())
