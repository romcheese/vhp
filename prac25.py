# https://skillsmart.ru/algo/lvl1/gc8b.html
# получает на вход массив из N (N >= 1) целых положительных
# чисел и возвращает true, если сумма всех значений
# результата двойной трансформации A чётная.
# А - массив случайных положительных чисел (могут повторяться)
def TransformTransform(A, N):
    def Transform_1(A, N):
        B = []
        for i in range(N-1):
            for j in range(N-i-1):
                k = i+j
                try:
                    B.append(max(A[j:k]))
                except ValueError:
                    pass
        return B
    x = Transform_1(A, N)
    y = sum(Transform_1(x, len(x)))
    if y % 2 == 0:
        return True
    return False
