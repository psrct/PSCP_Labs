'''Sequence IV'''
def main(num):
    '''Sequence IV'''
    start = 1
    for _ in range(num):
        for _ in range(num):
            print(start, end=" ")
            start += 1
        print("\n", end="")
main(int(input()))
