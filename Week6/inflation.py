'''Inflation'''
import math as m

def main():
    """Inflation Function"""
    money = float(input())
    years = int(input())
    percent = 0.0381
    for _ in range(years):
        money += money*percent
    money = money// 100
    print("%.2f" %money)

main()
