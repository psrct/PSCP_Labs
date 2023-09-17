'''Backward.py'''

def backward():
    '''Backward Function'''
    wordlist = []
    while True:
        word = input()
        if word == "NULL":
            break
        else:
            wordlist.append(word)
    wordlist.reverse()
    for i in wordlist:
        print(i)

backward()
