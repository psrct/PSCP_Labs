'''PlanCDEFGHIJKLMNOPQRSTUVWXYZ'''
def main(typesel, num1, num2, num3):
    '''Ascend or Descend'''
    num1, num2 = findmx(num1, num2)
    num1, num3 = findmx(num1, num3)
    num2, num3 = findmx(num2, num3)
    if typesel == "Ascend":
        print("%.2f, %.2f, %.2f" %(num3, num2, num1))
    else:
        print("%.2f, %.2f, %.2f" %(num1, num2, num3))

def findmx(number1, number2):
    '''Max'''
    if number2 > number1:
        return number2, number1
    else:
        return number1, number2
main(input(), float(input()), float(input()), float(input()))
