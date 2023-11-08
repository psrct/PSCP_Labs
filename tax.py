"""Tax"""

def main(ages, size):
    """Tax"""
    tax = 0
    if size >= 1801:
        tax += (size-1800) * 4
        size = 1800
    if 601 <= size <= 1800:
        tax += (size-600) * 1.5
        size = 600
    if 1 <= size <= 600:
        tax += size*0.5
    if ages == 6:
        tax -= 0.1*tax
    if ages == 7:
        tax -= 0.2*tax
    if ages == 8:
        tax -= 0.3*tax
    if ages == 9:
        tax -= 0.4*tax
    if ages >= 10:
        tax -= 0.5*tax
    print("%.2f"%tax)
main(int(input()), int(input()))
