'''isprime_small'''

def prime(number):
    '''Prime Function'''
    check = False
    for i in range(2, number):
        if number % i == 0:
            check = True
            break
    if check or number == 1:
        print("No")
    else:
        print("Yes")

prime(abs(int(input())))
