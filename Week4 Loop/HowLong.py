'''HowLong'''
def main(num):
    '''Number'''
    total = 0
    for i in str(num):
        for j in range(0, 10):
            if i == str(j):
                total += 1
    print(total)
main(int(input()))
