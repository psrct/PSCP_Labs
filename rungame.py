"""RunGame"""

def run_game(text):
    """RunGame"""
    total = 0
    for i in range(len(text)):
        total += abs(int(text[i]) - int(text[i-1])) if i else int(text[i])
    print(total)

run_game(input().split())
