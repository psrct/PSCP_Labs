'''AndAgain'''

def andagain(text):
    '''AndAgain Fucntion'''
    lis = text.replace(".", "").split()
    lis.sort()
    screen = False
    word = "aeiou"
    for i in lis:
        count = 0
        for j in i:
            if j.lower() in word:
                count += 1
        if count >= 2:
            print(i)
            screen = True
    if screen == False:
        print("Nope")

andagain(input())
