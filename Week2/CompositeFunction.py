'''CompositeFunction'''
def main():
    '''dasadf'''
    numx = int(input())
    f_gx = func1(function1, function2)
    g_fx = func2(function1, function2)
    print("%.2f" %f_gx(numx))
    print("%.2f" %g_fx(numx))
def func1(num_f, num_g):
    '''num_f(num_g(numx))'''
    return lambda numx: num_f(num_g(numx))
def func2(num_f, num_g):
    '''num_g(num_f(numx))'''
    return lambda numx: num_g(num_f(numx))
def function1(numx):
    '''num_f(numx)'''
    return 2 * numx
def function2(numx):
    '''num_g(numx)'''
    return numx / 2 + 1
main()
