"""Classify"""

def sort_the_id(this_id):
    """Sort the ID by years"""
    all_id = []
    non_dupe_id = []
    while this_id != "END":
        year_id = int(this_id[:2])
        faculty_id = int(this_id[2:4])
        all_id.append([year_id, faculty_id])
        if [year_id, faculty_id] not in non_dupe_id:
            non_dupe_id.append([year_id, faculty_id])
        this_id = str(input())
    all_id.sort()
    non_dupe_id.sort()
    prev_year = all_id[0][0] - 1
    for things in non_dupe_id:
        this_year = things[0]
        this_id = things[1]
        print(this_year if prev_year < this_year else "--", end=" ")
        prev_year = max(this_year, prev_year)
        print("{} {}".format(this_id, all_id.count(things)))

sort_the_id(str(input()))
