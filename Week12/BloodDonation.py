'''BloodDonation'''

def blood(age):
    '''BloodDonation Function'''
    if age == 17 or 60 <= age <= 70:
        weight = int(input())
        count = int(input())
        book = input()
        if book == "False":
            print("No")
        else:
            if weight >= 45:
                if count == 0 and age > 55:
                    print("No")
                else:
                    print("Yes")
            else:
                print("No")
    elif age > 17 and age < 60:
        weight = int(input())
        count = int(input())
        if weight >= 45:
            if count == 0 and age > 55:
                print("No")
            else:
                print("Yes")
        else:
            print("No")
    else:
        print("No")
blood(int(input()))
