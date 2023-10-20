"""Easy Histogram"""

def histogram(text):
    """Easy Histogram Function"""
    text_dict = {}
    for i in text:
        if i not in text_dict:
            text_dict.update({i: 1})
        else:
            text_dict[i] += 1
    sorted_dict = sorted(text_dict, key=lambda x: (x.lower(), x.swapcase()))
    for j in sorted_dict:
        print("{} = {}".format(j, text_dict.get(j)))

histogram(str(input()).replace(" ", ""))
