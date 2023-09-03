'''Largest Number'''
def findmx(num1, num2, num3):
    '''Max Value without max()'''
    mostvalue = int("%d%d%d" %(num1, num2, num3))
    if int("%d%d%d" %(num1, num3, num2)) > mostvalue:
        mostvalue = int("%d%d%d" %(num1, num3, num2))
    if int("%d%d%d" %(num1, num2, num3)) > mostvalue:
        mostvalue = int("%d%d%d" %(num1, num2, num3))
    if int("%d%d%d" %(num2, num1, num3)) > mostvalue:
        mostvalue = int("%d%d%d" %(num2, num1, num3))
    if int("%d%d%d" %(num2, num3, num1)) > mostvalue:
        mostvalue = int("%d%d%d" %(num2, num3, num1))
    if int("%d%d%d" %(num3, num2, num1)) > mostvalue:
        mostvalue = int("%d%d%d" %(num3, num2, num1))
    if int("%d%d%d" %(num3, num1, num2)) > mostvalue:
        mostvalue = int("%d%d%d" %(num3, num1, num2))
    print(mostvalue)
findmx(abs(int(input())), abs(int(input())), (abs(int(input()))))
