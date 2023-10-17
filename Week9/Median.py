"""Median"""

def main(count):
    "Median"
    numlis = []
    for _ in range(count):
        numlis.append(int(input()))
    numlis.sort()
    num = len(numlis)
    if num % 2 == 0:
        med = ((numlis[int((num/2)-1)]) + numlis[int(num/2)])/2
    else:
        med = numlis[int(num/2)]
    print(float(med))

main(int(input()))
