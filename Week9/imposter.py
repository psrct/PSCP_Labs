"""Impostor"""
import json

def make_dict(crew_status):
    """Make a dict of players"""
    ship_status = {}
    dead_list = []
    while crew_status != "Start":
        ship_status.update(json.loads(crew_status))
        crew_status = str(input())
    the_dead = str(input())
    while the_dead != "End":
        dead_list.append(the_dead)
        the_dead = str(input())
    return sorted(list(ship_status.items())), sorted(dead_list)

def who_is_imposter(crew_status):
    """PrintOut the status of the crews"""
    ship_status, dead_list = make_dict(crew_status)
    imposter_count = 0
    text_alive = ""
    text_dead = ""
    for crew in ship_status:
        crew_color = crew[0]
        crew_job = crew[1]
        if crew_color not in dead_list:
            text_alive += "{} : {}\n".format(crew_color, crew_job)
            if crew_job == "Impostor":
                imposter_count += 1
        else:
            text_dead += "{} : {}\n".format(crew_color, crew_job)
    out_text = "{} Impostor Remains\n".format(imposter_count) + "***Alive***\n" + text_alive +\
               "***Dead***\n" + text_dead
    print(out_text.strip())

who_is_imposter(str(input()))
