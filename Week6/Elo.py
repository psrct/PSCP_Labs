'''Elo'''

def elo(rate1, rate2, want):
    """Elo Function"""
    if want == "A":
        print("%.2f" %possi(rate2, rate1))
    else:
        print("%.2f" %possi(rate1, rate2))

def possi(rate_1, rate_2):
    """main"""
    result = (1/(1+10**((rate_1 - rate_2)/400)))
    return result

elo(int(input()), int(input()), input())
