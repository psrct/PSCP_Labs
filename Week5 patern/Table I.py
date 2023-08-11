'''Table I'''
def foodprice(count):
    '''15 * x'''
    for i in range(count):
        print("15 x {} = {}".format(i+1, 15*(i+1)))
foodprice(int(input()))
