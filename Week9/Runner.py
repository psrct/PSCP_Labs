"""Runner"""

def who_is_winning(court_length, contesters):
    """Find the one that win the running competition"""
    all_runner = []
    fastest_runner = []
    for _ in range(contesters):
        this_runner = str(input()).split()
        this_runner = list(map(int, this_runner))
        all_runner.append([this_runner[0], court_length - this_runner[1]])
    all_runner = list(enumerate(all_runner))
    all_runner.sort(key=lambda x: x[1][1]/x[1][0])
    fastest_pace = all_runner[0][1][1] / all_runner[0][1][0]
    fastest_runner = list(
        filter(lambda x: fastest_pace >= x[1][1]/x[1][0], all_runner))
    print(sorted(fastest_runner, reverse=True)[0][0] + 1)

who_is_winning(float(input()), int(input()))
