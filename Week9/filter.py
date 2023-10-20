"""Filter"""
import json

def score_filter(textdict, score):
    """Filter Function"""
    score_dict = json.loads(textdict)
    score_list = list(score_dict.items())
    score_list.sort(key=lambda x: int(x[0]))
    screen = False
    for i in score_list:
        if float(i[1]) < score:
            continue
        print("{}\t{:.2f}".format(i[0], i[1]))
        screen = True
    if screen is False:
        print("Nope")

score_filter(str(input()), float(input()))
