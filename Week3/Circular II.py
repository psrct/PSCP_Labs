'''Circular II'''

def main():
    '''2 circle'''
    numx_me = float(input())
    numy_me = float(input())
    radius1 = float(input())
    numx_fd = float(input())
    numy_fd = float(input())
    radius2 = float(input())
    distance = (((numx_me - numx_fd)**2) + ((numy_me - numy_fd)**2))** 0.5
    radius = radius1 + radius2
    if distance < radius or radius1 >= distance/2 <= radius2:
        print("Yes")
    else:
        print("No")
main()
