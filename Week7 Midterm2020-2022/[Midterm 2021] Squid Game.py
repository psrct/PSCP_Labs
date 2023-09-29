'''[Midterm 2021] Squid Game'''

def game():
    '''main'''
    teama = 0
    teamb = 0
    for _ in range(10):
        num1 = int(input())
        teama += num1
    for _ in range(10):
        num2 = int(input())
        teamb += num2
    if teama > teamb:
        print("B")
    elif teama < teamb:
        print("A")
    else:
        print("AB")

game()
