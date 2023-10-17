'''Matrix_MN'''

def matrixx(row, col):
    '''Matrix_MN Function'''
    for _ in range(row):
        for _ in range(col):
            print(input(), end=" ")
        print('\n', end=" ")
matrixx(int(input()), int(input()))
