# https://skillsmart.ru/algo/lvl1/d83i.html
def MatrixTurn(matrix, M, N, T):

    for i in range(len(matrix)):# иммутабельная матрица
        matrix[i] = list(matrix[i])

    if M > N: # ищем наименьшее значение
        min = N
    else:
        min = M

    m = matrix
    s = min//2 # количество траекторий/кругов


    for i in range(T):
        el = []
        for i in range(s): # третья переменная для алгоритма
            el.append(m[i][i])
        for i in range(s): # переключаем траектории змейки
            horiz = N-i*2-1
            vert = M-i-1
            for x in range(i, horiz):
                m[i][x+1],el[i] = el[i],m[i][x+1]
            for y in range(i, vert):
                m[y+1][horiz], el[i] = el[i], m[y+1][horiz]
            for x in range(i+1, horiz+1)[::-1]:
                m[vert][x-1],el[i] = el[i],m[vert][x-1]
            for y in range(i+1, vert+1)[::-1]:
                m[y-1][i],el[i] = el[i],m[y-1][i]

    for i in range(len(matrix)):
        matrix[i] = ''.join(matrix[i])

    return matrix


#
#
# x = MatrixTurn(["1234","4564","7894","1234","4564","7894"], 6,4, 16)
# print(x)
