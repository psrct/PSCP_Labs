'''[Midterm 2022] Parity'''
def bit8(data, choose):
    '''main'''
    bit1 = 0
    for i in data:
        if int(i) == 1:
            bit1 += 1
    if choose == "Even":
        if bit1 %2 == 0:
            data += "0"
        else:
            data += "1"
    elif choose == "Odd":
        if bit1 %2 != 0:
            data += "0"
        else:
            data += "1"
    print(data)
bit8(input(), input())
