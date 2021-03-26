
# TreeOfLife(3,4, 12, [".+..","..+.",".+.."])
# h-height, w-width, n-kolichestvo strok, tree-исходный список веток
def TreeOfLife(H:int, W:int, N:int, tree:list):
    d = 0
    tr = []
    for v in tree:
        e = []
        v = v.replace('.', '0')
        v = v.replace('+', '1')
        for el in v:
            e.append(int(el))
        tr.append(e)

    tree = tr # удобнее ссылаться

    while d != N:
        d += 1

        for v in tree: # старение
            for i in range(len(v)):
                v[i] += 1


        if d % 2 == 0:
            for i in range(H): # уничтожение
                vetka = tree[i] # рассматриваем ветку с индексом 0
                for y in range(W): # рассматриваем элементы поочередно
                    elem = vetka[y]
                    if elem >= 3:
                        try:
                            vetka[y] = 0
                            left = vetka[y-1]
                            right = vetka[y+1]
                            up = tree[i-1][y]
                            down = tree[i+1][y]
                            if y - 1 >= 0  and left < 3:
                                left = 0
                            if y + 1 <= W and right < 3:
                                right = 0
                            if y - 1 >= 0 and up < 3:
                                up = 0
                            if y + 1 <= H and down < 3:
                                down = 0
                        except IndexError:
                            pass


    tr = []
    for v in tree:
        vetka = ''
        for el in v:
            if el == 0:
                vetka += '.'
            else:
                vetka += '+'
        tr.append(vetka)
    return tr

#
#
# x = TreeOfLife(6, 7, 24, [".......","...+...","....+..",".......","++.....","++....."])
# x = TreeOfLife(3,4, 12, [".+..","..+.",".+.."])
# print(x)
