"""Kabata"""

def kabata_checker(text_amount):
    """https://youtu.be/NrI-UBIB8Jk?si=K5T5TeoOM6uah0Tf"""
    is_it_kabata_list = []
    for _ in range(text_amount):
        this_text = str(input())
        check = "yes"
        this_text = this_text.replace("bakka", "__").replace("baka", "!!!!")
        for char in range(0, len(this_text), 2):
            word = this_text[char:char + 2]
            if word not in ("ka", "ba", "ta", "__"):
                check = "no"
        is_it_kabata_list.append(check)
    print(*is_it_kabata_list, sep="\n")

kabata_checker(int(input()))
