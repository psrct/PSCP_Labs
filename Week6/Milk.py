"""[Recommend] Milk"""

def milk(bottleprice, bottle_cap, free, money):
    """Milk"""
    result = money//bottleprice
    get = result
    while get >= bottle_cap and free != 0:
        if bottle_cap == 0:
            break
        result += free
        get += free
        get -= bottle_cap
    print(result)

milk(int(input()), int(input()), int(input()), int(input()))
