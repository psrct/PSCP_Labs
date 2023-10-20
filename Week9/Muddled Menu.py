'''Muddled Menu'''

def muddle():
    '''Muddled Menu Function'''
    course = []
    while True:
        menu = input()
        if menu == "DONE":
            break
        elif menu == "CLOSED":
            course.clear()
            break
        elif menu == "SOMETHING'S WRONG":
            course.clear()
        elif "Can't do:" in menu:
            dot = menu.find(":") + 2
            course.remove(menu[dot:])
        else:
            dot = menu.find("#")
            if menu[dot +1:].isdigit():
                course.insert(int(menu[dot +1:])- 1, menu[:dot - 1])
            else:
                course.append(menu[:dot - 1])
    course_rev = course.copy()
    course_rev.reverse()
    print("Full Course: {} Reversed: {}".format(course, course_rev))

muddle()
