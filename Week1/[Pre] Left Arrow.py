'''Left Arrow'''
def main():
    '''<<<'''
    width = int(input())
    height = int(input())
    countdown = height//2
    if height % 2 != 0:
        for i in range(countdown):
            print((" " *  countdown) + (width * "*"))
            countdown -= 1
        print(width * "*")
        for i in range(height//2):
            print((" " *  (i + 1)) + (width * "*"))
main()
