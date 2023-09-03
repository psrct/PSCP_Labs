'''Largest Number'''
def findm(number1, number2):
    '''Max value'''
    return number1 if number1 > number2 else number2
def main(num1, num2, num3):
    '''Cats'''
    count1 = findm(int("%d%d%d" %(num1, num2, num3)), int("%d%d%d" %(num1, num3, num2)))
    count2 = findm(count1, int("%d%d%d" %(num2, num1, num3)))
    count3 = findm(count2, int("%d%d%d" %(num2, num3, num1)))
    count4 = findm(count3, int("%d%d%d" %(num3, num1, num2)))
    count5 = findm(count4, int("%d%d%d" %(num3, num2, num1)))
    print(count5)
main(abs(int(input())), abs(int(input())), abs(int(input())))
