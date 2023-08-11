'''Grade II'''
def main(num):
    '''0 - 100'''
    if num >= 95 and num <= 100:
        print("A")
    elif num >= 90 and num < 95:
        print("B+")
    elif num >= 85 and num < 90:
        print("B")
    elif num >= 80 and num < 85:
        print("C+")
    elif num >= 75 and num < 80:
        print("C")
    elif num >= 70 and num < 75:
        print("D+")
    elif num >= 65 and num < 70:
        print("D")
    elif num >= 60 and num < 65:
        print("F+")
    elif num >= 0 and num < 60:
        print("F")
    else:
        print("ERR")
main(float(input()))
