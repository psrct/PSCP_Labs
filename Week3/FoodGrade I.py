'''FoodGrade I'''
def main():
    '''chicken 24/2'''
    count = 0
    count += chicken_1()
    count += chicken_1()
    count += chicken_1()
    count += chicken_1()
    count += chicken_1()
    count += chicken_1()
    print(count)
def chicken_1():
    '''Count chicken'''
    count1 = 0
    chicken1 = int(input())
    chicken2 = int(input())
    chicken3 = int(input())
    chicken4 = int(input())
    if 70 >= chicken1 >= 50:
        count1 += 1
    if 70 >= chicken2 >= 50:
        count1 += 1
    if 70 >= chicken3 >= 50:
        count1 += 1
    if 70 >= chicken4 >= 50:
        count1 += 1
    return count1
main()
