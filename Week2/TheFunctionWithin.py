'''TheFunctionWithin'''
def main(numa, numb, numc, numd):
    '''Docstring'''
    print(f_xfunc(f_xfunc(numa)))
    print(g_xfunc(f_xfunc(numa - numb)))
    print(hfunc((f_xfunc(numa + numb)), f_xfunc(numa + numc), (g_xfunc(f_xfunc(numd**2)))))
    print(ifunc((hfunc((f_xfunc(numa + numb)), f_xfunc(numa - numc)
                       , g_xfunc(f_xfunc(numd**2)))), g_xfunc(f_xfunc(numa - numb))
                , f_xfunc(f_xfunc(f_xfunc(f_xfunc(f_xfunc(numc))))), numd**8))
def f_xfunc(numx):
    '''f(x)'''
    return 2 * numx
def g_xfunc(numx):
    '''g(x)'''
    return (3*numx**4) - (numx**3) + (2 * numx**2) + 10
def hfunc(numx, numy, numz):
    '''h(x,y,z)'''
    return ((numz + numx)**2) - (numx * numy) + (numy ** 2)
def ifunc(numa, numb, numc, numd):
    '''i(a, b, c, d)'''
    return (numa**2 + numb**2 - numc**2)/(numd**2 - (2 * numa * numd) + 2 * numa)
main(float(input()), float(input()), float(input()), float(input()))
