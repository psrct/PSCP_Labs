'''Duplicate I'''

def duplicate(group1, group2):
    '''Duplicate I Function'''
    group11 = set()
    group22 = set()
    for _ in range(group1):
        group11.add(input())
    for _ in range(group2):
        group22.add(input())
    if  group11.intersection(group22):
        intersec = group11.intersection(group22)
        lis = [i for i in intersec]
        lis.sort(reverse=True)
        for j in lis:
            print(j)
    else:
        print("Nope")

duplicate(int(input()), int(input()))
