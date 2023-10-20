'''RemoveTag'''

def retag(text):
    '''RemoveTag Function'''
    lis = []
    if "<" in text or ">" in text:
        for _ in range(text.count("<")):
            text = text[text.find(">") + 1:]
            lis.append(text[:text.find("<")].strip())
    else:
        lis = text.split()
    print(" ".join(lis).split())

retag(input())
