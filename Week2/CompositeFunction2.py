'''CompositeFunction'''
def main():
    '''CompositeFunction'''
    numx = int(input())
    print("%.2f" %ffunc(gfunc(numx)))
    print("%.2f" %gfunc(ffunc(numx)))
def ffunc(numx):
    '''f(x)'''
    return 2 * numx
def gfunc(numx):
    '''g(x)'''
    return numx / 2 + 1
main()
