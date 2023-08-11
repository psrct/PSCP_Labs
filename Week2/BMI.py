'''BMI'''
def main():
    '''Body Mass index'''
    bmi()
    bmi()
    bmi()
    bmi()
    bmi()
def bmi():
    '''bmi'''
    name = input()
    weight = float(input())
    tall = float(input())
    print(name + "\'s  BMI = %.2f" %(weight / (tall/100)**2))
main()
