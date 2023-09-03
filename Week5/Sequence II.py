'''Sequence II'''
def main(num):
    '''3,5,7,9'''
    number = 1
    number2 = 3
    for _ in range(num):
        print(number, end=" ")
        number += number2
        number2 += 2
main(int(input()))
