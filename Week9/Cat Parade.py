'''Cat Parade'''

def parade():
    '''Cat Parade Function'''
    catlist = ""
    while True:
        cats = input()
        if cats == "END":
            break
        else:
            catlist += cats + "," or cats[1:] if " " in cats
    catlist = catlist.split(",")
    while True:
        if "IT'S A DOG" in catlist:
            dog = catlist.index("IT'S A DOG")
            catlist.remove("IT'S A DOG")
            catlist.pop(dog-1)
        else:
            catlist.remove("")
            catlist.sort()
            break
    for i in catlist:
        print(i)
parade()
