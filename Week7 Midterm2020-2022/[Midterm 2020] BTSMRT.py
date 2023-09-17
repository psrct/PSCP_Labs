'''[Midterm 2020 + Recommend] BTSMRT'''

def pay(day, age, height):
    '''pay function'''
    if age < 14 and height < 90:
        print("FREE")
    elif age < 14 and height <= 140 and day == "Children Day":
        print("FREE")
    elif day == "Senior Day" and age >= 60:
        print("FREE")
    else:
        print("PAY")

pay(input(), float(input()), float(input()))
