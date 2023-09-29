'''[Midterm 2022] Coke'''

def coke(price, cap, promo, get):
    '''Coke'''
    total = 0
    if cap == 0:
        print(price * get)
        return
    for i in range(get):
        if i != 0 and i % cap == 0:
            total += promo
            continue
        total += price
    print(total)

coke(int(input()), int(input()), int(input()), int(input()))
