"""GCD_v1"""

def calculate(num1, num2):
    '''ห.ร.ม'''
    minnum = min(num1, num2) if min(num1, num2) > 0 else max(num1, num2)
    for i in range(minnum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            print(i)
            break
calculate(int(input()), int(input()))
