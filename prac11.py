# Нарушен принцип повторяемости кода из-за спешки
# https://skillsmart.ru/algo/lvl1/s81f.html


def BigMinus(s1, s2):

    if s1 == s2:
        return '0'

    equal = False

    if len(s1) < len(s2):
        s1,s2 = s2,s1

    elif len(s1) == len(s2):
        if int(s1) < int(s2): # возможно тут есть biginteger
            s1,s2 = s2,s1
        equal = True

    s1 = [int(i) for i  in s1]
    s2 = [int(i) for i in s2]

    if equal == False:
        diff = len(s1) - len(s2)
        result = s1[:diff]
        s1 = s1[diff:]

        for i in range(len(s1)):

            if s1[i] > s2[i]:
                x = s1[i] - s2[i]
                result.append(x)

            elif s1[i] < s2[i]:
                k = -1
                while True:
                    if result[k] == 0:
                        result[k] -= 1
                        k -= 1
                    elif result[k] != 0:
                        result[k] -= 1
                        break
                x = s1[i] + 10 - s2[i]
                result.append(x)

            elif s1[i] == s2[i]:
                result.append(0)

        s = ''
        for i in result:
            s += str(i)

        s = int(s)
        s = str(s)
        return type(s)

    elif equal == True:

        result = []

        for i in range(len(s1)):

            if s1[i] > s2[i]:
                x = s1[i] - s2[i]
                result.append(x)

            elif s1[i] < s2[i]:
                k = -1
                while True:
                    if result[k] == 0:
                        result[k] -= 1
                        k -= 1
                    elif result[k] != 0:
                        result[k] -= 1
                        break
                x = s1[i] + 10 - s2[i]
                result.append(x)

            elif s1[i] == s2[i]:
                result.append(0)
        s = ''
        for i in result:
            s += str(i)

        s = int(s)
        s = str(s)
        return s

x = BigMinus('1234567891', '1')
print(x)

#
# x = BigMinus(s1, s2)
# print(x)
# ________
    # Здесь нам нужно решить, какая из строк больше по длине, и не равны ли они вовсе.
    # equal = False
    # if len(s1) > len(s2):
    #     pass
    # elif len(s1) < len(s2):
    #     s1,s2 = s2,s1
    # elif len(s1) == len(s2):
    #     for i in range(len(s1)):
    #         if s1[i] == s2[i]:
    #             if s1 == s2:
    #                 return '0'
    #             equal = True
    #             continue
    #         elif s1[i] > s2[i]:
    #             break
    #         elif s1[i] < s2[i]:
    #             s1,s2 = s2,s1
    #
    # if equal == False:
    #     # Нашли разницу лен, чтобы найти сравниваемые участки
    #     diff = len(s1) - len(s2)
    #
    #     result = s1[:diff] # результирующая переменная
    #     s1 = s1[diff:] # cравниваемая часть
    #
    #     # Cравниваем по-индексно
    #     for i in range(len(s1)):
    #         if s1[i] >= s2[i]:
    #             x = s1[i] - s2[i]
    #         elif s1[i] < s2[i]:
    #             result[-1] -= 1
    #             x = 10-s2[i]
    #         result.append(x)
    #     return result
    #
    # elif equal == True: # equal len
    #     for i in range(len(s1)):
    #         if s1[i]  == s2[i]:
    #             continue
    #         elif s1[i] > s2[i]:
    #
# ________ last ver
