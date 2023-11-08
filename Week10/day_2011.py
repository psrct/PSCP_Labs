"""Day2011"""

def day_in_2011(date, month):
    """main"""
    month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 30}
    day_dict = {0:"Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday",
                4: "Wednesday", 5: "Thursday", 6: "Friday"}
    that = sum(month_dict.get(i) for i in range(1, month)) + date - 1
    print(day_dict.get(that % 7))

day_in_2011(int(input()), int(input()))