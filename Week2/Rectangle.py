'''Rectangle'''
def main(var_h, var_w):
    '''function'''
    square(var_h, var_w)
    rectangle(var_h, var_w)
def square(var_h, var_w):
    '''Docstring1'''
    print(var_h * var_w)
def rectangle(var_h, var_w):
    '''Docstring2'''
    print(2 * (var_h + var_w))
main(int(input()), int(input()))
