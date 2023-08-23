'''Frame'''
def frame(word):
    '''Frame'''
    print("*" * (len(word) + 2))
    print("*" + word + "*")
    print("*" * (len(word) + 2))

frame(input())
