'''PH'''

def ph_calculate(number):
    '''PH Function'''
    if 0 <= number < 7:
        print("acidic")
    elif number == 7:
        print("neutral")
    elif 7 < number <= 14:
        print("akaline")
    else:
        print("error")

ph_calculate(float(input()))
