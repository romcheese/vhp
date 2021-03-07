# https://skillsmart.ru/algo/lvl1/gc8b.html
# получает на вход массив из N (N >= 1) целых положительных
# чисел и возвращает true, если сумма всех значений
# результата двойной трансформации A чётная.
# А - массив случайных положительных чисел (могут повторяться)
def TransformTransform(A, N):
    def Transform(A, N):
        B = []
        for i in range(N):
            for j in range(N-i):
                k = i+j
                try:
                    B.append(max(A[j:k+1]))
                except ValueError:
                    pass
        return B

    x = Transform(a, len(a))
    y = sum(Transform(x, len(x)))

    if y%2 == 0:
        return True
    else:
        return False
