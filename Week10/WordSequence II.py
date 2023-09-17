'''WordSequence II'''

def sequence2(word1, word2):
    '''Sequence II Function'''
    print(word1)
    for i in range(len(word1)):
        text = (word2[0: i+1] + word1[i+1 :])
        print(text)
    if len(word1) < len(word2):
        for i in range(len(word1), len(word2)):
            print(text + word2[len(word1): i+1])

sequence2(input(), input())
