"""Easy Histogram (No Dict)"""

def histogram(text):
    """Count the letter in text"""
    histolist = []
    upper_list = []
    for char in text:
        if char not in histolist and char.isalpha():
            histolist.append(char)
            if char.isupper():
                upper_list.append(char)
    histolist = list(map(str.lower, histolist))
    histolist.sort()
    sleeper = histolist.copy()
    for things in histolist:
        if things.upper() in upper_list:
            if histolist.count(things) > 1:
                print("{} = {}".format(things, text.count(things)))
                sleeper.remove(things)
            print("{} = {}".format(things.upper(), text.count(things.upper())))
            upper_list.remove(things.upper())
            sleeper.remove(things)
        elif things in sleeper:
            print("{} = {}".format(things, text.count(things)))
            sleeper.remove(things)

histogram(str(input()))
