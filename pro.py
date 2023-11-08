'''pro'''

def pro(head_pro, paid, per_person, head):
    """Pro"""
    print(((head%head_pro) + (head//head_pro)*paid) * per_person)
pro(int(input()), int(input()), int(input()), int(input()))
