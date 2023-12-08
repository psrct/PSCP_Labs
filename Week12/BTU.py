'''BTU'''

def btu_calcu(area):
    '''calculate btu'''
    if area in range(100, 151):
        btu = 5000
    elif area in range(151, 251):
        btu = 6000
    elif area in range(251, 301):
        btu = 7000
    elif area in range(301, 351):
        btu = 8000
    elif area in range(351, 401):
        btu = 9000
    elif area in range(401, 451):
        btu = 10000
    elif area in range(451, 551):
        btu = 12000
    elif area in range(551, 701):
        btu = 14000
    else:
        btu = btu_calcu2(area)
    return btu

def btu_calcu2(area):
    '''calculate btu'''
    if area in range(701, 1001):
        btu = 18000
    elif area in range(1001, 1201):
        btu = 21000
    elif area in range(1201, 1401):
        btu = 23000
    elif area in range(1401, 1501):
        btu = 24000
    elif area in range(1501, 2001):
        btu = 30000
    elif area in range(2001, 2501):
        btu = 34000
    return btu

def calofbtu(site, height, person, heat, sunset):
    '''BTU'''
    allbtu = btu_calcu(site) + (1000 * max(height - 8, 0)) + \
    (600 * max(person - 2, 0)) + (4000 * (heat == "kitchen"))
    if sunset == "facing the sun":
        allbtu += allbtu * 0.1
    elif sunset == "shaded":
        allbtu -= allbtu * 0.1
    print(int(allbtu))

calofbtu(int(input()), int(input()), int(input()), input(), input())
