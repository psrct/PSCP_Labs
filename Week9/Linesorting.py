"""LineSorting"""

def main(count):
    "Sort the line"
    textlis = []
    for _ in range(count):
        textlis.append(str(input()))
 
    text = len(textlis)
    textlis.sort(key=len)
    for text in range(len(textlis)):
        print(textlis[text])

main(int(input()))
