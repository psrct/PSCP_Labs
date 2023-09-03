'''Sequence III'''
def main(num):
    '''Sequence III'''
    start = 1
    for _ in range(num):
        start += 1
        for i in range(start, num + start):
            print(i, end=" ")
        print("\n", end="")
main(int(input()))
