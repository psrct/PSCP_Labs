'''[Midterm 2020] BigFrame'''

def bigframe():
    '''BigFrame Function'''
    word1 = input().strip()
    word2 = input().strip()
    word3 = input().strip()
    word4 = input().strip()
    word5 = input().strip()
    long = max(len(word1), len(word2), len(word3), len(word4), len(word5))
    print("*" * (4 + long))
    print("* %s%s *" %(word1, " " * (long-len(word1))))
    print("* %s%s *" %(word2, " " * (long-len(word2))))
    print("* %s%s *" %(word3, " " * (long-len(word3))))
    print("* %s%s *" %(word4, " " * (long-len(word4))))
    print("* %s%s *" %(word5, " " * (long-len(word5))))
    print("*" * (4 + long))

bigframe()
