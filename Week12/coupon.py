"""Coupon"""
def money(price, abc, xyz):
    """money function help mom"""
    abc = abc.split(" ")
    xyz = xyz.split(" ")
    price1 = price
    price2 = price
    if price >= float(abc[1]):
        price1 -= float(abc[0])
    if price >= float(xyz[1]):
        price2 -= price*float(xyz[0])/100
    if price1 == price and price2 == price:
        print("Nope")
    elif price1 < price2:
        print("1 %.1f" %price1)
    else:
        print("2 %.1f" %price2)

money(float(input()), input(), input())
