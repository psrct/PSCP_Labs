'''Robot I'''
def main(name, age):
    '''age < 18 == pass'''
    if age < 18 and age > 0:
        print("{}, you can pass.".format(name))
    else:
        print("{}, you shall not pass.".format(name))
main(input(), float(input()))
