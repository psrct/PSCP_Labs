'''[Recommend] ValidVar'''

def creatname(number):
    '''Vaili or Invalid'''
    for _ in range(number):
        word = input()
        if word == "if" or word == "else"\
            or word == "elif" or word == "while" or word == "for"\
            or word == "True" or word == "False" or word == "continue" or word == "break"\
                or word == "return" or word == "is" or word == "in" or word == "and"\
                    or word == "or" or word == "from" or word == "as" or word == "pass"\
                        or word == "not" or word == "def" or word == "None":
            print("Invalid")
        elif word.isidentifier():
            print("Valid")
        else:
            print("Invalid")

creatname(int(input()))
