'''ball'''

def ball(height):
    '''BALL'''
    count = 0
    while True:
        height *= 3/5
        if height >= 0.01:
            count += 1
        else:
            break
    print(count)

ball(float(input()))
