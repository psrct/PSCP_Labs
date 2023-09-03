'''Virus I'''
def cal_virus(word):
    '''lowercase o'''
    count = 0
    for i in word:
        if i == "o":
            count += 1
    print(count)

cal_virus(input())
