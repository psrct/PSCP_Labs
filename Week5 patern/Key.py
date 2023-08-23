'''Key'''
def key(number):
    '''Key'''
    total = 0
    for i in number:
        total += int(i)
    number = number[10:]
    number = int(number) * 10
    result = total + number
    if result <= 1000:
        print(result + 1000)
    elif result > 9999:
        result = str(result)[1:]
        print(result)
    else:
        print(result)

key(input())
