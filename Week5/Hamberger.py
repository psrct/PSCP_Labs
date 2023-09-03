'''Hamberger'''

def hamberger(left, right):
    ''' | = bread, * = meat'''
    print("|" * left + "*" * ((left +right) *2) + "|" * right)

hamberger(int(input()), int(input()))
