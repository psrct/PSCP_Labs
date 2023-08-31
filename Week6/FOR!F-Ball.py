'''FOR!F-Ball'''
def ball(word):
    '''where's ball'''
    numa = True
    numb = False
    numc = False
    for i in word:
        if i == "A":
            if numa or numb:
                numa = not numa
                numb = not numb
        elif i == "B":
            if numb or numc:
                numb = not numb
                numc = not numc
        elif i == "C":
            if numa or numc:
                numa = not numa
                numc = not numc
    if numa:
        print("1")
    elif numb:
        print("2")
    elif numc:
        print("3")

ball(input())
