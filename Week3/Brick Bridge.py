'''Brick Bridge'''
def main(small, big, goal):
    '''Brick Bridge'''
    if goal // 5 >= big:
        goal = goal - (big * 5)
    else:
        goal = goal - ((goal // 5)*5)

    if goal <= small:
        print(goal)
    else:
        print("-1")

main(int(input()), int(input()), int(input()))
