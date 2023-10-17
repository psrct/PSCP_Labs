"""Seeker"""

def seeker():
    """Seeker function"""
    text = input()
    digit = ""
    total = 0
    for char in text:
        if char.isdigit():
            digit += char
        else:
            total += int(digit) if len(digit) > 0 else 0
            digit = ""
    total += int(digit) if len(digit) > 0 else 0
    print(total)
seeker()
