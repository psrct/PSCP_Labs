'''Cat Parade'''

def parade():
    '''Cat Parade Function'''
    animal = []
    while True:
        cat = input()
        if cat == "END":
            break
        elif "," in cat:
            cat = cat.split(", ")
            animal.extend(cat)
        else:
            animal.append(cat)
    while True:
        if "IT'S A DOG" in animal:
            dog = animal.index("IT'S A DOG")
            animal.pop(dog)
            animal.pop(dog-1)
        else:
            break
    catlist = animal.copy()
    catlist.sort()
    for i in range(len(catlist)):
        if catlist[i] == catlist[i-1] and i != 0:
            continue
        else:
            print("{} {} {}".format(catlist[i], (animal.index(catlist[i])+1)\
                , catlist.count(catlist[i])))

parade()
