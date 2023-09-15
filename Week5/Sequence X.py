"""Sequence X"""

def main():
    """Sequence X"""

    num = int(input())
    default = 1
    check = 0
    number = num

    for i in range(num*2 - 1):
        for j in range(num*2 - 1):
            if i+j >= num-1 and j <= num-1 and i < num:
                print("%02d" %default, end=" ")
                if j < num-1:
                    default += 1
            elif j-i <= num-1 and j > num-1 and i < num:
                default -= 1
                print("%02d" %default, end=" ")
            elif j+i > number and j <= num-1 and i >= num:
                print("%02d" %default, end=" ")
                if j < num-1:
                    default += 1
                check = 1
            elif j > num-1 and i >= num and (num + num*2-2) - (i+j) > 0:
                default -= 1
                print("%02d" %default, end=" ")
            else:
                print("%2s" %" ", end=" ")
        print()

        default = 1
        if check > 0:
            number += 2
            check = 0

main()
