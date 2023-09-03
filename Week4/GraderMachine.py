'''GraderMachine'''
def main(start, stop):
    '''pair number'''
    num_sum = 0
    num_pass = ""
    step = 1
    if stop < start:
        step = -1
        stop -= 1
    else:
        stop += 1
    for i in range(start, stop, step):
        if i % 2 == 0:
            num_pass += "%d " %i
            num_sum += i
    print("pass : %s\nSum : %d" %(num_pass, num_sum))
main(int(input()), int(input()))
