'''[Recommend] Blackjack'''

def blackjack(num):
    '''[Recommend] Blackjack'''
    total = 0
    check = 0
    for _ in range(num):
        card = input()
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            total += 11
            check += 1
        else:
            total += int(card)
    for _ in range(check):
        if total > 21:
            total -= 10
    print(total)

blackjack(int(input()))
