'''[Midterm 2023] Home Run'''
def homerun(num, batter):
    '''[Midterm 2023] Home Run'''
    count = 0
    for _ in range(num):
        place = float(input())
        if place < batter:
            count += 1
    print(count)
homerun(int(input()), float(input()))
