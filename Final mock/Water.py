'''Water'''

def water(month, price, ifmore):
    '''Water'''
    more_price = float(input())
    not_pay = float(input())
    total_pay = 0
    for _ in range(month):
        unit = float(input())
        allprice = unit * price
        more_unit = unit - 5
        price_more_unit = more_unit * more_price
        if allprice > not_pay:
            if unit > ifmore:
                total_pay += price_more_unit + (price * 5)
    print("%0.2f" %total_pay)

water(int(input()), float(input()), float(input()))
