'''Seven'''
def main():
    '''7 ** x'''
    number()
def number():
    '''power of 2'''
    num = int(input())
    if num % 4 == 0:
        print(1)
    elif num % 4 == 1:
        print(7)
    elif num % 4 == 2:
        print(9)
    elif num % 4 == 3:
        print(3)
main()
