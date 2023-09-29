'''[Midterm 2020 + Recommend] Phone Number'''

def phone(num, word):
    '''PhoneNumber Function'''
    if len(num) == 9:
        if word == "Domestic":
            print(num[0], num[1:5], num[5:])
        else:
            print("+66", num[1:5], num[5:])
    else:
        if word == "Domestic":
            print(num[:2], num[2:6], num[6:])
        else:
            print("+66"+ num[1], num[2:6], num[6:])

phone(input(), input())
