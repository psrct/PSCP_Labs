'''Roman'''

def roman(text):
    '''Roman function'''
    numdict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    before = numdict[text[0]] + 1
    total = 0
    for i in text:
        number = numdict[i]
        if before < numdict[i]:
            total += number - (before * 2)
        else:
            total += number
        before = number
    print(total)

roman(str(input()).upper())
