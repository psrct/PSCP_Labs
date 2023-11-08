'''BTU'''

def btu(area, height, people, heat, sun):
    '''BTU calculate'''
    btu = 0
btu(int(input()), int(input()), int(input()), str(input()), str(input()))

def areana(area):
    btu = 0
    if 100 <= area <= 150:
        btu = 5000
    elif 151 <= area <= 250:
        btu = 6000
    elif 251 <= area <= 300:
        btu = 7000
    elif 301 <= area <= 350:
        btu = 8000
    elif 351 <= area <= 400:
        btu = 9000
    elif 401 <= area <= 450:
        btu = 10000
    elif 451 <= area <= 550:
        btu = 12000
    elif 551 <= area <= 700:
        btu = 14000
    elif 701 <= area <= 1000:
        btu = 18000
    elif 1001 <= area <= 1200:
        btu = 21000
    elif 