'''Stepper II'''
def main(start, stop):
    '''|m-n| + 1 line'''
    if start > stop:
        for i in range(start, stop-1, -1):
            print(i)
    else:
        for i in range(start, stop+1):
            print(i)
main(int(input()), int(input()))
