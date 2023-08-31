'''[Recommend] RockPaperScissor'''
def score(hands):
    '''RP SP PR'''
    playa = 0
    playb = 0
    while hands != "":
        if hands[:2] == "SP":
            playa += 1
        elif hands[:2] == "PR":
            playa += 1
        elif hands[:2] == "RS":
            playa += 1
        elif hands[:2] == "SR":
            playb += 1
        elif hands[:2] == "PS":
            playb += 1
        elif hands[:2] == "RP":
            playb += 1
        hands = hands[2:]
    win(playa, playb)
def win(playa, playb):
    '''score'''
    if playa > playb:
        print("A win %d-%d" %(playa, playb))
    elif playb > playa:
        print("B win %d-%d" %(playb, playa))
    else:
        print("DRAW %d" %playa)

score(input())
