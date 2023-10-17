"""CoPrimeV1"""

def calculate(num1, num2):
    '''ห.ร.ม'''
    minnum = min(num1, num2) if min(num1, num2) > 0 else max(num1, num2)
    for i in range(minnum, 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            ans = i
            break
    if ans == 1:
        print("YES")
    else:
        print("NO")
    print(ans)

calculate(int(input()), int(input()))
