"""Point Sorting"""

def sort_method(that_list):
    """x + y"""
    x_var, y_var = that_list[0], that_list[1]
    return int(x_var) + int(y_var), int(y_var) * -1

def sort_the_point(point):
    """Sort the point by <e>judge method"""
    point_list = []
    point_list_sort = []
    for _ in range(point):
        for _ in range(int(input())):
            that_pos = str(input()).split()
            if that_pos not in point_list:
                point_list.append(that_pos)
        point_list_temp = sorted(point_list, key=sort_method)
        point_list_sort.append(point_list_temp)
        point_list.clear()
    for things in point_list_sort:
        for another in things:
            print(*another, sep=" ")

sort_the_point(int(input()))
