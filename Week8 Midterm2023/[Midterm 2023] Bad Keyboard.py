'''[Midterm 2023] Bad Keyboard'''

def keyboard(word):
    '''Bad Keyboard'''
    text = ""
    for i in word:
        if i == "i":
            text += "o"
        elif i == "o":
            text += "i"
        elif i == "O":
            text += "I"
        elif i == "I":
            text += "O"
        else:
            text += i
    print(text)

keyboard(input())
