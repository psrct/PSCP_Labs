'''iPad Air'''

def ipad(color, mem, net):
    '''iPad Air Function'''
    liscolor = ["Space Gray", "Silver", "Green", "Rose Gold", "Sky Blue"]
    if color not in liscolor:
        print("Not Available")
    else:
        if mem == "64" and net == "Wi-Fi":
            print("19900")
        elif mem == "64" and net == "Wi-Fi + Cellular":
            print("24400")
        elif mem == "256" and net == "Wi-Fi":
            print("24900")
        elif mem == "256" and net == "Wi-Fi + Cellular":
            print("29400")
        else:
            print("Not Available")
ipad(input(), input(), input())
