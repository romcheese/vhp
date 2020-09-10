def ConquestCampaign(N:int, M:int, L:int, battalion:list):
    squares = []
    l_b = []
    r_b = []
    u_b = []
    d_b = []
    coords = []
    if N*M < 4:
        return 1

    #_____1____
    for i in range(1, N+1): # all squares
        for y in range(1, M+1):
            squares.append([i,y])

    #_____2____
    for i in range(1, M+1): # left and right borders
        l_b.append([0,i])
        r_b.append([N+1,i])

    for i in range(1, N+1): # up and down borders
        u_b.append([i, M+1])
        d_b.append([i, 0])

    #_____3____
    for i in range(len(battalion)): # parsing coordinates
        if i % 2 == 0 or i == 0:
            x = battalion[i]
        else:
            y = battalion[i]
            coords.append([x,y])

    #_____4____
    checked_coords = []

    for i in coords:
        if i not in checked_coords:
            checked_coords.append(i)

    coords = checked_coords


    colored = coords
    days = 1

    while len(colored) != len(squares):

        for i in range(len(coords)):

            x = coords[i][0]
            y = coords[i][1]


            r = [x+1, y] # правая клетка
            l = [x-1, y]
            u = [x, y+1]
            d = [x, y-1]

            if r not in r_b and r not in colored:
                colored.append(r)

            if l not in l_b and l not in colored:
                colored.append(l)

            if u not in u_b and u not in colored:
                colored.append(u)

            if d not in d_b and d not in colored:
                colored.append(d)

        days +=1
    return days

# x = ConquestCampaign(N = 3, M = 4, L = 2, battalion = [2,2,3,4])
# print(x)



# _____________GARBAGE:































    #
    # while len(colored) != len(squares):
    #
        # x = coords[c][0]
        # y = coords[c][1]
        #
        #
        # r = [x+1, y] # правая клетка
        # l = [x-1, y]
        # u = [x, y+1]
        # d = [x, y-1]
        #
        # if r not in r_b and r not in colored:
        #     colored.append(r)
        #
        # if l not in l_b and l not in colored:
        #     colored.append(l)
        #
        # if u not in u_b and u not in colored:
        #     colored.append(u)
        #
        # if d not in d_b and d not in colored:
        #     colored.append(d)
    #
    #      c += 1






#
#
#


    #




    # coords = []
    # days = 0
    # squares = []
    # b_upper = []
    # b_down = []
    # b_left = []
    # b_right = []
    # colored = []
    #
    # for i in range(1, N+1): # all squares
    #     for y in range(1, M+1):
    #         squares.append([i,y])
    #
    # for i in range(len(battalion)): # coordintates -> coords
    #     if i % 2 == 0 or i == 0:
    #         x = battalion[i]
    #     else:
    #         y = battalion[i]
    #         coords.append([x,y])
    #
    # for i in range(1, M+1): # left, right borders
    #     l_b = [0, i]
    #     r_b = [N+1, i]
    #     b_left.append(l_b)
    #     b_right.append(r_b)
    #

# получает первыми двумя параметрами размер Государства Квадратов NxM,
# а battalion содержит массив из L*2 целых чисел (L >= 1) с индексацией с нуля,
# в котором каждый чётный элемент содержит очередную координату области высадки
# по первому измерению N, а каждый нечётный элемент содержит очередную
# # координату области высадки по второму измерению M.
# Не исключено, что в связи с неразберихой в командовании координаты областей
# высадки могут дублироваться.
# На примере с картинки параметры будут такими:
# N = 3, M = 4, L = 2, battalion = [2,2, 3,4]
# Возвращает функция день, начиная с 1,
# когда все области будут взяты под контроль.

# какое решение предлагается?
# N - x, M - y

# 1) Записываем все возможные координаты
# 2) Очерчиваем границы
# 3) Парсим координаты
# 4) Закрашиваем. Отмечаем
# 5) Проверяем клетки на закрашенность и границы, если проходит, то закрашиваем
