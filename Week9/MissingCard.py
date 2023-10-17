'''MissingCard'''

def findcard():
    '''MissingCard Fuction'''
    group = set()
    text = set()
    for _ in range(51):
        text.add(input())
    for i in ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']:
        for j in ["S", "H", "D", "C"]:
            group.add(i+j)
    print(*(group.difference(text)))

findcard()
