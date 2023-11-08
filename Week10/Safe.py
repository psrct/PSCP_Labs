'''Safe'''
 
def safe(text, lock):
    '''Safe Function'''
    count = 0
    for i in range(len(text)):
        number = abs((ord(text[i])) - (ord(lock[i])))
        number26 = 26 - (number)
        count += min(number, number26)
    print(count)
 
safe(str(input()), str(input()))
