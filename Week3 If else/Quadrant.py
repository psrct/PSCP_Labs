'''Quadrant'''
def main(num_x, num_y):
    '''X, Y'''
    if num_x > 0 and num_y > 0:
        print("Q1")
    elif num_x < 0 and num_y > 0:
        print("Q2")
    elif num_x < 0 and num_y < 0:
        print("Q3")
    elif num_x > 0 and num_y < 0:
        print("Q4")
    elif num_x > 0 or num_x < 0 and num_y == 0:
        print("X")
    elif num_y > 0 or num_y < 0 and num_x == 0:
        print("Y")
    elif num_x == 0 and num_y == 0:
        print("O")
main(int(input()), int(input()))
