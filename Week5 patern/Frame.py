'''Frame'''
def main(word):
    '''Frame'''
    picture = "*" * len(word)
    print("{0}\n{1}\n{0}".format(picture, word))
main(input())
