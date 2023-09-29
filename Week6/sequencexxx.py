"""SequencXXX"""

def seqx(size, volumn):
    """xXXXx"""
    for i in range(size):
        for _ in range(volumn):
            for k in range(size):
                if i == k or k == 0 or k == size-1 or i+k == size-1 or \
                    i == 0 or i == size-1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print(" ", end="")
        print()

seqx(int(input()), int(input()))
