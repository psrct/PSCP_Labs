'''[Midterm 2023] Lift'''

def lift(people, highest):
    '''[Midterm 2023] Lift'''
    count = 0
    total = 0
    for _ in range(people):
        age = int(input())
        weight = float(input())
        if age >= 12:
            count += 1
        total += weight
    if count > 0 and total <= highest:
        print("Safe")
    elif people == 0:
        print("Safe")
    else:
        print("Not Safe")
lift(int(input()), float(input()))
