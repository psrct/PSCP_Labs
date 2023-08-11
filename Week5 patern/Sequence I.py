'''Sequence I'''
def main(num):
    '''Sequence I'''
    word = ""
    for i in range(num):
        word += str(i + 1) + " "
    for _ in range(num):
        print(word)
main(int(input()))
