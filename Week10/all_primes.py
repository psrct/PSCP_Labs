"""All_Primes"""

def allprimes():
    """All_Primes funciton"""
    count = 0
    num = int(input())
    for digit in range(2, num+1):
        check = False
        for index in range(2, digit):
            if digit % index == 0:
                check = True
                break
        if not check:
            count += 1
    print(count)

allprimes()
