'''Donut'''
def price_donut(price, number, free, require):
    '''Price of Donut'''
    box = number + free
    price_box = price * number
    number_box = require // box
    remain = require - (number_box * box)
    if remain >= number:
        number_box += 1
        remain = 0
    pay = number_box * price_box + (remain * price)
    numdonut = number_box * box + remain
    print(pay, numdonut)
price_donut(int(input()), int(input()), int(input()), int(input()))
