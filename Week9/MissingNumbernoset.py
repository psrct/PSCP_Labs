'''MissingNumber'''

def missing(end):
    '''MissingNumber Function'''
    numlist = []
    new = []
    allnum = [i for i in range(1, end+1)]
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            numlist.append(num)
    number = [new.append(j) for j in allnum if j not in numlist]
    new.sort()
    for num in new:
        print(num)
    number.clear()

missing(int(input()))
