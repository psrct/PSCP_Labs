'''WeightStation'''
def main(sumtruck, num2, num3, num4):
    '''Truck'''
    num1 = (sumtruck * 4) - (num2 + num3 + num4)
    sum2 = sumtruck / 2
    if num1 + (num2 + num3 + num4) > 15000:
        print("Overweight")
    elif abs(num1 - sumtruck) > sum2 or abs(num2 - sumtruck) > sum2 or\
        abs(num3 - sumtruck) > sum2 or abs(num4 - sumtruck) > sum2:
        print("Unbalance")
    else:
        print("Pass %.2f" %num1)
main(float(input()), float(input()), float(input()), float(input()))
