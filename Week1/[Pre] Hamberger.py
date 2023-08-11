'''Hamberger'''

def main():
    '''pork'''
    lbread = int(input())
    rbread = int(input())
    bread1 = (lbread + rbread) * "*"
    print((lbread * "|") + bread1 * 2 + (rbread * "|"))
main()
