'''Kayak'''
def main():
    '''player'''
    number = int(input())
    weight = input().split(" ")
    total = 0
    for _ in range(2*number):
        weight[_] = int(weight[_])
    weight_sorted = sorted(weight)
    for i in range(number-1):
        total = total + (int(weight_sorted[i*2+1])-int(weight_sorted[i*2]))
    print(abs(total))
    print(weight_sorted)
main()
def main2():
    """main2"""
    volume = int(input())
    lst = input().split(" ")
    for k in range(2*volume):
        lst[k] = int(lst[k])
    lst = sorted(lst)
    check = 0
    ans = 0
    num_diff = 0
    while True:
        if len(lst) > 2:
            for i in range(len(lst) - 1):
                if abs(lst[i] - lst[i+1]) == num_diff:
                    ans += num_diff
                    lst.pop(i)
                    lst.pop(i)
                    check = 1
                    break
        else:
            break
        if check == 1:
            check = 0
        else:
            num_diff += 1
    print(ans)
main2()
