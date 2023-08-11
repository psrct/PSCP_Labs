'''arrow'''
def main():
    '''arrow short'''
    width = int(input())
    height = int(input())
    middle = height // 2
    for i in range(height):
        print(" " * abs(middle - i) + "*" * width)
main()
