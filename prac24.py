

def MatrixTurn(matrix, M, N, T):
    global Matrix
    for i in range(len(matrix)):# иммутабельная матрица
        matrix[i] = list(matrix[i])
    if M > N: # ищем наименьшее значение
        min = N
    else:
        min = M
    m = matrix
    s = min//2 # количество траекторий/кругов
     # задаем начальную позицию для алгоритма

    for c in range(T):
        el = []
        for i in range(s): # "плавающая" переменная для алгоритма
            el.append(m[i+1][i])
        for i in range(s): # переключаем траектории змейки
            h = N-i*2-1 # количество горизонт итераций на данной траектории при данной длине строки
            v = M-i*2-1 # количество вертик итераций на данной траектории при данной высоте

            hs = N-i-1 # позиция реверсивного горизонтального элемента
            vs = M-i-1 # -//- вертик

            for x in range(i, h+i):
                m[i][x], el[i] = el[i], m[i][x]
            for y in range(i, v+i):
                m[y][hs], el[i] = el[i], m[y][hs]
            for x in range(i, h+i)[::-1]:
                m[vs][x+1], el[i] = el[i], m[vs][x+1]
            for y in range(i, v+i)[::-1]:
                m[y+1][i],el[i] = el[i],m[y+1][i]

    for i in range(len(matrix)):
        matrix[i] = ''.join(matrix[i])

    Matrix = matrix
    return Matrix
#
# x = MatrixTurn(['123456','234567','345678','456789'], 4,6,16)
# for m in Matrix:
#     print(m)

# ключевая идея: исходить не из больших матрица, а из самой маленькой из возможхных,
# чтобы корректно сформировать абстракции, которые мы потом будем оборачивать в решение
# Ключ здесь: четыре базовые точки - углы. Они будут всегда в этой задаче.

# переключаем траектории змейки
# KEY_IDEA = Одна итерация = ОДНА замена ячейки
# Передвигаемся к следующей ячейке только циклом for.
# На одной итерации происходит просто замена текущего элемента на прошлый:
# Движение производится циклом
