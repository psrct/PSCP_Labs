'''Day I'''
def main(year):
    '''2 month = 29 day'''
    if (year % 400 == 0) or (year % 4 == 0) and (year % 100 != 0):
        print("Yes")
    else:
        print("No")
main(int(input()))
