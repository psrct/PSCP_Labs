'''AlmostMean'''

def almostmean(num):
    '''AlmostMean Function'''
    number = {}
    scorelist = []
    total = 0
    for _ in range(num):
        text = input().split()
        scorelist.append(float(text[1]))
        number.update({float(text[1]):text[0]})
        total += float(text[1])
    mean = total / num
    scorelist.append(mean)
    scorelist.sort()
    nearmean = scorelist.index(mean) - 1
    print("{}\t{}".format(number[scorelist[nearmean]], scorelist[nearmean]))

almostmean(int(input()))
