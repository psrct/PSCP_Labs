'''[Recommended] 113'''

def deletenum(number):
    '''delete113 function'''
    while "113" in number:
        number = number.replace("113", "")
    print(number)

deletenum(str(input()))
