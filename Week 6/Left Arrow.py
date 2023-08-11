'''Left Arrow'''
def arrow(width, high):
    '''Left Arrow'''
    middle = high // 2
    for i in range(high):
        print(" " * abs(middle - i) + "*" * width)

arrow(int(input()), int(input()))
