'''Helloooo'''

def hello(text):
    '''Helloooo Functions'''
    text = list(text)
    text_rev = text.copy()
    text_rev.reverse()
    lisout = []
    count = 0
    word = ["a", "e", "i", "o", "u"]
    for i in text_rev:
        if i in word:
            if count == 1:
                lisout.append(i)
                continue
            else:
                lisout.extend([i, i, i, i])
                count = 1
        else:
            lisout.append(i)
    lisout.reverse()
    print(*lisout, sep="")

hello(str(input()))
