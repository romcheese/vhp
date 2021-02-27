
# TreeOfLife(3,4, 12, [".+..","..+.",".+.."])
# h-height, w-width, n-kolichestvo strok, tree-исходный список веток
def TreeOfLife(H:int, W:int, N:int, tree):
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

    def plus(tree): # старение на год
        for v in tree:
            for i in range(len(v)):
                v[i] += 1

    def dead(tree):
        for i in range(H):
            vetka = tree[i] # рассматриваем ветку с индексом 0
            for y in range(W): # рассматриваем элементы поочередно
                elem = vetka[y]
                if elem >= 3:
                    try: # решение не изящное, но пока что успеваю так
                        vetka[y] = 0
                        if vetka[y-1] < 3:
                            vetka[y-1] = 0
                        if vetka[y+1] < 3:
                            vetka[y+1] = 0
                        if tree[i+1][y] < 3:
                            tree[i+1][y] = 0
                        if tree[i-1][y] < 3:
                            tree[i-1][y] = 0
                    except IndexError:
                        pass

    while d != N:
        d += 1
        plus(tree) # старение

        if d % 2 == 0:
            dead(tree)
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
# x = TreeOfLife(3,4, 4, [".+..","..+.",".+.."])
# print(x)
