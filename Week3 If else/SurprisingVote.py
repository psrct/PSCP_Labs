'''SurprisingVote'''
def surpris(total, highscore):
    '''highest middle lowest'''
    middle_score = min(total - highscore, highscore)
    lowscore = total - highscore - middle_score
    if highscore - lowscore > 2:
        print("Surprising")
    else:
        print("Not surprising")
surpris(float(input()), float(input()))
