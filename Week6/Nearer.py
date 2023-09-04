'''Nearer'''

def near(alice, bob, icecream):
    '''Who nearer'''
    if abs(icecream - alice) < abs(icecream-bob):
        print("Alice {}".format(abs(icecream-alice)))
    elif abs(icecream - alice) > abs(icecream-bob):
        print("Bob {}".format(abs(icecream-bob)))
    else:
        print("Sundaes {}".format(abs(icecream - alice)))

near(int(input()), int(input()), int(input()))
