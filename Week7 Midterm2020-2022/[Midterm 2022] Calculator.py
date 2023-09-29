'''[Midterm 2022] Calculator'''
def calculator(text):
    '''Calculator Function'''
    count = 0
    if text == 1:
        print(1)
        return

    for i in range(1, text+1):
        count += len(str(i)) + 1
    print(count)

calculator(int(input()))
