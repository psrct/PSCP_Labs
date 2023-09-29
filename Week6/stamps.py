"""Stamps"""

def main():
    """paid"""
    times = int(input())
    every_pay = int(input())
    get = int(input())
    everys = int(input())
    discount = int(input())
    stamps = 0
    total = 0

    for _ in range(times):
        if everys == 0:
            canuse = stamps
        else:
            canuse = stamps // everys
        bill = int(input())
        for _ in range(canuse):
            bill -= discount
            stamps -= everys
            if bill <= 0:
                bill = 0
                break
        if every_pay != 0:
            stamps += (bill // every_pay) * get
        else:
            stamps += bill * get
        total += bill
    print(total)
    print(stamps)

main()
