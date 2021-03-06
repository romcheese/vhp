# MatrixTurn(["123456", "234567", "345678", "456789"], 4,6, 3)
# M-строк, N-длина строки, T-шагов
# Минимальное значение из чисел M,N обязательно чётно
# кругов вразения будет столько, сколько же и минимальное значение или ширины или высоты // 2
def MatrixTurn(matrix, M, N, T):
    if M > N:
        min = N
    if N > M:
        min = M
    else:
        min = M

    if N == min and N % 2 == 0: # последний круг будет состоять из лево-право
        pass
    # сделать отдельнно обработку кода с x*2, точнее для кода,
    # у которого одна единсветнная траектория
    l = []
    r = []
    u = []
    d = []
    for i in range(min//2): # запарсили
        left = [x[i] for x in matrix[i:M-i]]
        right = [x[N-1-i] for x in matrix[i:M-i]]
        up = [x for x in matrix[i][i+1:-1-i]]
        down = [x for x in matrix[M-i-1][i+1:-1-i]]
        l.append(''.join(left))
        r.append(''.join(right))
        u.append(''.join(up))
        d.append(''.join(down))

    #____до сюда все корректно

    circles = [] # Траектории
    for i in range(min//2): # 0,1,2,3
        circle = ''
        circle += str(l[i])
        circle += str(d[i])
        circle += str(r[i])
        circle += str(u[i])
        circles.append(circle)

    # print(circles)

    for i in range(len(circles)): # 0,1,2 Поворот
        circles[i] = circles[i][T:]+circles[i][:T]
    #___________Переводим в список, чтобы можно было иммутить
    l_circles = []
    for circle in circles:
        l_circles.append(list(circle)) # хотя походу это было делать необязатнльо

    l_matrix = []
    for stroka in matrix:
        l_matrix.append(list(stroka))

    left = []
    right = []
    down = []
    up = []
#_______корректные уже развернутые значения иммутабельные  left
    for i in range(len(circles)): # 2 круга, две итерации
        x = M-i*2
        y = N-2-i*2
        left.append(circles[i][0:x])
        down.append(circles[i][x:x+y])
        right.append(circles[i][x+y:x*2+y])
        up.append(circles[i][x*2+y:])

    #____Key idea: распологать всю траекторию на каждой итерации, количетсов которых равно количеству траекторий
    for i in range(len(circles)): # 0,1
        x = len(left[i])
        for z in range(x): # меняем левую и правую часть на развернутую
            l_matrix[z+i][i] = left[i][z]
            l_matrix[z+i][N-1-i] = right[i][z]

        l_matrix[i][i+1:N-i-1] = up[i]
        l_matrix[M-i-1][i+1:N-i-1] = down[i]


    for i in range(len(matrix)): # преобразование
        matrix[i] = ''.join(l_matrix[i])

    # for m in matrix:
    #     print(m)

    return matrix




#
#
matrix = ["123456",
          "567891",
          "912323",
          "567845"]
# #
# # # ["123456", "234567", "345678", "456789"], 4,6, 3
# # # ["1234560", "2345670", "3456780", "4567890"] # не проходит
# #
x = MatrixTurn(matrix, 4,6, 20)
# print(x)
# ['2345678987654321', '45676543']
# print(x)
# 1 2 3 4 5 6
# 9 8 5 5 6 7
# 3 4 5 6 7 8
# 4 5 6 7 8 9
# x = MatrixTurn(matrix, 6, 8, 3)
# # (['12345678', '345679', '5678'], ['45236712', '212346', '6789'])
# matrix = ["12345678",
#           "23456798",
#           "34567862",
#           "45678951",
#           "42123463",
#           "45236712"]
