'''binary'''

def bary(num):
    '''bary function'''
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return str(bary(num//2)) + str(num%2)

print(bary(int(input())))
