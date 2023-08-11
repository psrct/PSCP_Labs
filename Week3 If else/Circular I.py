'''Circular I'''
def main(numx, numy, radius, numxn, numyn):
    '''distance'''
    dist = (((numxn - numx)**2) + ((numyn - numy)**2))** 0.5
    print("Yes" if radius >= dist else "No")
main(float(input()), float(input()), float(input()), float(input()), float(input()))
