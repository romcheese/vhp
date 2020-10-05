# s = 'нестнаьв'
# s = 'омшнл тоеее дйлмн акеен йокдо'
# s = 'омоюу толл дюиа акчп йрьк'
# https://skillsmart.ru/algo/lvl1/ab53.html
import math


def TheRabbitsFoot(s, encode):
    if encode == True:
        s = s.replace(' ', '') # удаляем пробелы
        sqr = len(s) ** 0.5
        # а что если лен  == 16. То верхняя и нижняя граница == 4.
        lb = math.floor(sqr) # находим нижнюю границу, число строк
        ub = math.ceil(sqr) # находим верхнюю границу, число столбцов

        while True: # определяем матрицу
            if lb * ub < len(s):
                lb += 1
            else:
                break

        phrase = []
        i = 0

        while True:
            if i >= len(s):
                break

            slice = s[:ub]
            phrase.append(slice)
            s = s[ub:]

        encode = ''

        for i in range(ub):
            for word in phrase:
                try:
                    encode += word[i]
                except IndexError:
                    continue
            encode += ' '
        encode = encode.strip()
        return encode
    elif encode == False:

        words = s.split()
        biggest_i = 0

        for word in words:
            i = len(word)
            if i > biggest_i:
                biggest_i = i

        decode = ''
        for i in range(biggest_i):
            for word in words:
                try:
                    decode += word[i]
                except IndexError:
                    continue

        return decode
