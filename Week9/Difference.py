'''Difference'''

def diff(num1, num2):
    '''Difference Function'''
    grouba = (int(input()) for _ in range(num1))
    groubb = (int(input()) for _ in range(num2))
    print(*sorted(set(grouba).difference(set(groubb))))

diff(int(input()), int(input()))
