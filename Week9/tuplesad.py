"""Tuple's Sad life"""

def main():
    "build รูปสุดเท่"
    numtup = tuple(str(input()).split())
    find = str(input())
    long = numtup.count(find)
    num = numtup.index(find)
    for _ in range(long):
        for _ in range(long):
            print(num, end=" ")
        print()

main()
