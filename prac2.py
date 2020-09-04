def odometer(array):
    distance = 0
    for i in range(len(array)):
        if i == 0 or i % 2 == 0:
            distance += array[i]
        else:
            continue
    return distance
