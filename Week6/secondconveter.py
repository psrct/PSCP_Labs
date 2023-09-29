"""Seconds converter"""
def convert(time, sec, minu, hours):
    """Secondonvert Time"""

    second = time
    minute = second // sec
    second = second % sec
    hour = minute // minu
    minute = minute % minu
    hour = hour % hours
    print("%d:%d:%d" %(hour, minute, second))

convert(int(input()), int(input()), int(input()), int(input()))
