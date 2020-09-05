# Каждый чётный элемент содержит скорость в километрах в час.
# Каждый нечётный элемент содержит время, прошедшее с начала поездки, в часах.
# Возвращает функция общее пройденное расстояние.
# на входе массив [10,1,20,2], на выходе расстояние 30.

def odometer(*args):

    array_type = type(args[0])

    distance = 0
    lasttime = 0
    result = 0

    if array_type == int:
        for i in range(len(args)):
            if i % 2 == 0 or i == 0:
                distance = args[i]
            else:
                result += (distance*(args[i]-lasttime))
                lasttime = args[i]
        return result

    elif array_type == list or array_type == tuple:
        array = args[0]
        for i in range(len(array)):
            if i % 2 == 0 or i == 0:
                distance = array[i]
            else:
                result += (distance*(array[i]-lasttime))
                lasttime = array[i]
        return result
    return None
