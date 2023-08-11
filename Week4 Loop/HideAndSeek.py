'''HideAndSeek'''
def main(start, end, step):
    '''step walk'''
    for i in range(start, end, step):
        print(i)
main(int(input()), int(input()), int(input()))
