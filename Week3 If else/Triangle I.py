'''Triangle I'''
def main(num1, num2, num3):
    '''Triangle I'''
    num1, num2 = findmx(num1, num2)
    num1, num3 = findmx(num1, num3)
    num2, num3 = findmx(num2, num3)
    print(trian(num3, num2, num1))

def trian(number1, number2, number3):
    '''built Triangle I'''
    if number1**2 + number2**2 == number3**2 or\
        number3**2 - 0.01 <= number1**2 + number2**2 <= number3**2 + 0.01:
        return "Yes"
    else:
        return "No"

def findmx(number1, number2):
    '''Max'''
    if number2 > number1:
        return number2, number1
    else:
        return number1, number2
main(float(input()), float(input()), float(input()))
