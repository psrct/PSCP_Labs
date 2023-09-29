'''PongYa'''

def pong(num):
    '''PongYa Function'''
    if num % 3 == 0:
        print("PONG")
    elif str(num)[-1] == "3":
        print("PONG")
    else:
        print(num)

pong(int(input()))
