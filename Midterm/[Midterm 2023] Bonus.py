'''[Midterm 2023] Bonus'''

def bonus(salary, year, months):
    '''B O N U S'''
    total = 0
    if months >= 10:
        year += 1
    if year > 20:
        year = 20
    if year == 0:
        total += salary
    else:
        total += (salary * year)
    if total > 1000000:
        total = 1000000
    elif total < 5000:
        total = 5000
    print(total)

bonus(int(input()), int(input()), int(input()))
