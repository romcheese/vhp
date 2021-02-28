# https://skillsmart.ru/algo/lvl1/o83c.html
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
                            if vetka[y-1] < 3 and (y-1) >= 0:
                                vetka[y-1] = 0
                            if vetka[y+1] < 3 and (y+1) >= 0:
                                vetka[y+1] = 0
                            if tree[i+1][y] < 3 and (i+1) >= 0:
                                tree[i+1][y] = 0
                            if tree[i-1][y] < 3 and (i-1) >= 0:
                                tree[i-1][y] = 0
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
#x = TreeOfLife(6,7, 2, [".......","...+...","....+..",".......","++.....","++....."])
#print(x)
