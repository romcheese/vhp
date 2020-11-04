# 10, 2, [[3,5,5], [5,2,2]]
# https://skillsmart.ru/algo/lvl1/a9d8.html
def Unmanned(L:int, N:int, track:list):

    lights = {}
    abs_time = 0

    for light in track:
        lights[light[0]] = [light[1], light[2]]

    for i in range(L):
        if i in lights:
            temp_time = 0
            array = lights[i]
            while  True:
                x = temp_time + array[0]
                if abs_time in range(temp_time, x+1):
                    abs_time = x
                    break
                else:
                    temp_time = x
                    x = temp_time + array[1]
                    if abs_time in range(temp_time, x+1):
                        break
        abs_time += 1

    return abs_time

#
# x = Unmanned(10, 2, [[3,0,0], [5,0,0]])
# print(x)
