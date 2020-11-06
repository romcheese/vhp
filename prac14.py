# 10, 2, [[3,5,5], [5,2,2]]
# https://skillsmart.ru/algo/lvl1/a9d8.html
def Unmanned(L:int, N:int, track:list):

    lights = {}
    abs_time = 0

    for light in track:
        lights[light[0]] = [light[1], light[2]]

    for i in range(L):
        if i in lights:
            n_p = 0
            array = lights[i]
            while True:
                k_p = n_p + array[0]
                if abs_time in range(n_p, k_p+1):
                    abs_time = k_p
                    break
                else:
                    n_p = k_p
                    k_p = n_p + array[1]
                    if abs_time in range(n_p, k_p+1):
                        break
                    n_p = k_p
        abs_time += 1


    return abs_time
#
# #
# # x = Unmanned(10, 2, [[3,5,5], [5,2,2]])
# x = Unmanned(10, 2, [[3,6,2],[6,2,2]])
# print(x)
