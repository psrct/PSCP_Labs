'''BootSequence'''
def main(num):
    '''keyword argument'''
    for i in range(1, num):
        print(i, end="_")
    print(num)
main(int(input()))
