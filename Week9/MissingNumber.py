'''MissingNumber'''

def missing(end):
    '''MissingNumber Function'''
    numset = set()
    allnum = {i for i in range(1, end+1)}
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            numset.add(num)
    diff = allnum.difference(numset)
    diff = list(diff)
    diff.sort()
    for i in diff:
        print(i)

missing(int(input()))
