'''MissingCard (No Set)'''

def findcard():
    '''MissingCard (No Set)'''
    group = []
    for i in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for j in ["S", "H", "D", "C"]:
            group.append(i+j)
    for _ in range(51):
        group.remove(input())
    print(*group)

findcard()
