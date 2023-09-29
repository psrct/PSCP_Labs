'''[Midterm 2020] One For All'''

def oneforall(num):
    '''ONE for all'''
    text = ""
    for i in range(1, num+1):
        name = input()
        text += name
        if num == i:
            text += "_" + str(i)
        elif i %2 == 1:
            text += ("*" * i)
        else:
            text += ("-" * i)
    print(text)

oneforall(int(input()))
