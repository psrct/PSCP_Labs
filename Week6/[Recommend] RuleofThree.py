'''[Recommend] RuleofThree'''

def ruleof3(count, price1, size1):
    '''RuleofThree Function'''
    value1 = size1/price1
    for _ in range(count-1):
        price2 = float(input())
        size2 = float(input())
        value2 = size2/price2
        if value2 >= value1:
            if price2 >= price1 and value2 == value1:
                pass
            else:
                price1 = price2
                size1 = size2
                value1 = value2
    print("%.2f %.2f" %(price1, size1))

ruleof3(int(input()), float(input()), float(input()))
