'''AscendingSort'''

def ascend():
    '''Ascend Function'''
    numlist = []
    for _ in range(5):
        num = int(input())
        numlist.append(num)
    numlist.sort()
    for i in numlist:
        print(i)

ascend()
