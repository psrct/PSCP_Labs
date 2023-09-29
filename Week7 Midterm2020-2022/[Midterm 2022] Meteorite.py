'''[Midterm 2022] Meteorite'''
def shoot(weight, number, lower):
    '''number * ? = weight'''
    shot = 0
    count = 0
    while not weight < lower:
        weight = weight / number
        shot += number ** count
        count += 1
    print(shot)

shoot(float(input()), int(input()), float(input()))
