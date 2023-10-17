'''AlmostMean'''

def almostmean(num):
    '''AlmostMean Function'''
    lisscore = []
    means = 0
    for _ in range(num):
        text = input()
        lisscore.append(float(text))
        means += float(text[1])
    means /= num
    lisscore.append(means)
    for i in lisscore:
        print(i)
almostmean(int(input()))
