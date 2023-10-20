'''HorizontalHistogram'''

def horizon_zerodawn(text):
    """Make a graph"""
    text_list = sorted(set(list(text)))
    for char in text_list:
        print(char.swapcase() + " : ", end="")
        for count in range(text.count(char)):
            amount = count + 1
            print("-", end="")
            if amount % 5 == 0 and amount != text.count(char):
                print("|", end="")
        print()

horizon_zerodawn(str(input()).swapcase())
