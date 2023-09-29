'''Parallelogram'''

def paral(text):
    '''Parallelogram Function'''
    index = ""
    for i in range(len(text)):
        index += text[i]
        print((" " * ((len(text)-1)-i)) + index)
    for j in range(1, len(text)):
        print(index[j:])
paral(input())
