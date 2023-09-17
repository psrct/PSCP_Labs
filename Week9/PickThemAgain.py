'''PickThemAgain'''

def convert(text):
    '''Convert Function'''
    list1 = []
    for i in text:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            list1.append(int(i))
    list1.reverse()
    if list1 == []:
        print("Nope")
    else:
        for i in list1:
            print(i)

convert(input().split())
