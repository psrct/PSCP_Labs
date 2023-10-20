"""BusStop I"""

def stop_bus(passengers, stop):
    """Count the passengers that get to desired stop"""
    current_passengers = []
    all_stop = []
    passengers_count = 0
    for _ in range(stop):
        get_stop = str(input()).split()
        get_stop = list(map(int, get_stop))
        all_stop.append([get_stop[0], get_stop[1:]])
    all_stop.sort()
    for current_stop in all_stop:
        if current_stop[0] in current_passengers:
            for _ in range(current_passengers.count(current_stop[0])):
                current_passengers.remove(current_stop[0])
                passengers_count += 1
        for people in current_stop[1]:
            bus_size = len(current_passengers)
            if bus_size < passengers and people > current_stop[0]:
                current_passengers.append(people)
            elif bus_size >= passengers:
                break
    print(passengers_count)

stop_bus(int(input()), int(input()))
