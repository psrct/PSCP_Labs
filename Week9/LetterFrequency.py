'''LetterFrequency'''

def letter(text):
    '''LetterFrequency'''
    alphabet = []
    uselist = []
    most = {}
    for i in text:
        if i.isalpha() and i not in alphabet:
            alphabet.append(i)
            uselist.append(text.count(i))
            most.update({text.count(i): i})
    uselist.sort()
    print(most[uselist[len(uselist)-1]])

letter(str(input()))
