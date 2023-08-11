'''Grader Machine2'''
def main(numberx, numbery):
    '''numberx : numbery or numbery : numberx'''
    total = 0
    print("pass :", end=" ")
    if numberx > numbery:
        for i in range(numberx, numbery-1, -1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    else:
        for i in range(numberx, numbery+1):
            if i % 2 == 0:
                print(i, end=" ")
                total += i
    print("\nSum :", total)
main(int(input()), int(input()))
