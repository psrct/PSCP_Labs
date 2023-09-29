'''Diginity'''

def rfidcard():
    '''Diginity Function'''
    while True:
        num = input()
        if num != "0":
            while True:
                num = check(num)
                if num < 10:
                    print(num)
                    break
                else:
                    num = str(num)
        else:
            break

def check(number):
    '''loop check'''
    result = 0
    for i in range(len(number)):
        result += int(number[i])
    return result

rfidcard()
