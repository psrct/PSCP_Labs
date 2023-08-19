'''ChristmasTree'''
def numtree(tree, height):
    '''ChristmasTree'''
    space = tree
    for i in range(tree):
        print(" " * (tree-1) + "*" * ((i*2) + 2-1))
        tree -= 1
    for _ in range(height):
        print((" " * (space - 2)) + "---")

numtree(int(input()), int(input()))
