'''Blackjack'''
def main():
    '''Blackjack'''
    count = int(input())
    total = 0
    haveacena = 0
    for _ in range(count):
        num = input()
        if num.isdecimal():
            total += int(num)
        elif num == "A":
            total += 11
            haveacena += 1
        elif num == "J" or "Q" or "K":
            total += 10
    for _ in range(haveacena):
        if total > 21:
            total -= 10
    print(total)
main()
        