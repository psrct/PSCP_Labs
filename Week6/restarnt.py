'''Resturant'''

def money():
    '''Money Function'''
    bill = float(input())
    every = float(input())
    discount = float(input())
    more = float(input())
    total = bill + more
    bill_discount = ((100-discount)/100)
    if total >= every:
        total = total*bill_discount
    if bill >= every:
        bill = bill*bill_discount
    if bill < total:
        print("No %.3f" %abs(bill - total))
    elif bill > total:
        print("Yes %.3f" %abs(total-bill))
    else:
        print("Yes")

money()
