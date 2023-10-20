'''BreachTheDoor'''

def door(longtext):
    '''BreachTheDoor Function'''
    all_text = longtext.split()
    textlist = []
    for word in all_text:
        for j in word:
            if not j.isalnum() or j.isdigit():
                word = word.replace(j, "")
        long = len(word)
        if long > 6:
            textlist.append(word)
    print(" ".join(textlist))

door(input())
