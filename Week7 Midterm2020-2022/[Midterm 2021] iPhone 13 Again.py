'''iPhone 13 Again'''

def pay(gen1, memory1):
    '''Price iphon 13 Function'''
    if gen1 == "iPhone 13 mini":
        ip13mini(memory1)
    elif gen1 == "iPhone 13":
        ip13(memory1)
    elif gen1 == "iPhone 13 Pro":
        ip13pro(memory1)
    elif gen1 == "iPhone 13 Pro Max":
        ip13promax(memory1)
    else:
        print("Not Available")

def ip13mini(memory):
    '''iPhone 13 mini'''
    if memory == "128 GB":
        print("25900")
    elif memory == "256 GB":
        print("29900")
    elif memory == "512 GB":
        print("37900")
    else:
        print("Not Available")

def ip13(memory):
    '''iPhone 13'''
    if memory == "128 GB":
        print("29900")
    elif memory == "256 GB":
        print("33900")
    elif memory == "512 GB":
        print("41900")
    else:
        print("Not Available")

def ip13pro(memory):
    '''iPhone 13 Pro'''
    if memory == "128 GB":
        print("38900")
    elif memory == "256 GB":
        print("42900")
    elif memory == "512 GB":
        print("50900")
    elif memory == "1 TB":
        print("58900")
    else:
        print("Not Available")

def ip13promax(memory):
    '''iPhone 13 Pro Max'''
    if memory == "128GB":
        print("42900")
    elif memory == "256 GB":
        print("46900")
    elif memory == "512 GB":
        print("54900")
    elif memory == "1 TB":
        print("62900")
    else:
        print("Not Available")

pay(input(), input())
