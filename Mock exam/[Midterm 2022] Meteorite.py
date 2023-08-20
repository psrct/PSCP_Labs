'''[Midterm 2022] Meteorite'''
def shoot(weight, number, lower):
    '''number * ? = weight'''
    count = 1
    small = weight / number
    power = small
    while small > lower:
        small = small/power
        count += number
    print(count)

shoot(float(input()), int(input()), float(input()))
