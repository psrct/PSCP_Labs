'''Turnstile'''

def main():
    '''Main Function'''
    stat = "lock"
    passnum = 0
    while True:
        action = input()
        if action == "C" and stat == "lock":
            stat = "unlock"
        elif action == "P" and stat == "unlock":
            stat = "lock"
            passnum += 1
        elif action == "END":
            break
    print(passnum)

main()
