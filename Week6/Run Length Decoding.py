'''Run Length Decoding'''

def decoding(text):
    '''Decoding Function'''
    count = ""
    wordout = ""
    for index in text:
        if index.isdecimal():
            count += index
        else:
            word = index * int(count)
            wordout += word
            count = ""
    print(wordout)

decoding(input())
