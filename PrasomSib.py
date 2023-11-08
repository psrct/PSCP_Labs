'''PrasomSib'''

def prasom(text_number):
    '''prasom'''
    number = 0
    count = 0
    for i in range(len(text_number)):
        if number == 10:
            count += 1
            number = 0
        elif number < 10:
            number += int(text_number[i])
        elif number == 0:
            number += int(text_number[i-1]) + int(text_number[i])
        elif number > 10:
            number 
    print(number)

prasom(str(input()))