"""Lotto"""

def main():
    """Check how much you get"""
    lotto1 = input()
    lottolast_2 = input()
    lottofront_3 = [input(), input()]
    lottolast_3 = [input(), input()]
    lotto = input()
    reward = 0
    if lotto1 == "999999":
        near = ["999998", "000000"]
    elif lotto1 == "000000":
        near = ["000001", "999999"]
    else:
        near_t = int(lotto1)+1
        near_1 = "%06d" %near_t
        near_t = int(lotto1)-1
        near_2 = "%06d" %near_t
        near = [near_1, near_2]
    if lotto == lotto1:
        reward += 6000000
    elif lotto in near:
        reward += 100000
    if lotto[4:6] == lottolast_2:
        reward += 2000
    if lottofront_3[0] == lottofront_3[1]:
        if lotto[0:3] in lottofront_3:
            reward += 8000
    else:
        if lotto[0:3] in lottofront_3:
            reward += 4000
    if lottolast_3[0] == lottolast_3[1]:
        if lotto[3:6] in lottolast_3:
            reward += 8000
    else:
        if lotto[3:6] in lottolast_3:
            reward += 4000
    print(reward)

main()
