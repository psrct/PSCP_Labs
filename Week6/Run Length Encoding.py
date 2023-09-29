'''Run Length Encoding'''

def encoding(text):
    '''Encoding Function'''
    index = "%s" %text[0]
    count = 0
    wordout = ""
    for i in text:
        if index == i:
            count += 1
        elif index != i:
            wordout += "{}{}".format(count, index)
            count = 1
            index = i
    wordout += "{}{}".format(count, index)
    print(wordout)

encoding(input())
