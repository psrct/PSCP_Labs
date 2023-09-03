'''SumOfNumber'''
def main(num_limit):
    '''numx != -1 , sum != limit'''
    num_sum = 0
    while True:
        numx = int(input())
        if numx == -1:
            break
        num_sum += numx
        if num_sum == num_limit:
            break
    print(num_sum)
main(int(input()))
