'''Socks'''

def socks(text):
    '''find pairs of socks'''
    socklist = []
    text = list(text)
    text.sort()
    longtext = ""
    for i in text:
        longtext += i
    for _ in range(len(longtext)):
        if len(longtext) > 1:
            if longtext[0] == longtext[1]:
                socklist.append(longtext[:2])
                longtext = longtext[2:]
            else:
                longtext = longtext[1:]
        else:
            break
    if len(socklist) == 0:
        print("None")
        print(len(socklist))
    else:
        print(*socklist)
        print(len(socklist))

socks(str(input()))
