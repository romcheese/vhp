# на входе может быть массив int, list как в prac2.py


def MadMax(*args):

    if type(args[1]) == list or type(args[1]) == tuple:

        N = args[0]

        lst = sorted(args[1])
        new_list = lst[:N//2]
        second_part = lst[N//2:][::-1]

        for i in second_part:
            new_list.append(i)

        return new_list

    elif type(args[1]) == int:

        N = args[0]
        array = []

        for i in args[1:]:
            array.append(i)

        array = sorted(array)

        new_list = array[:N//2]
        second_part = array[N//2:][::-1]

        for i in second_part:
            new_list.append(i)

        return new_list




# 
#
# x = MadMax(11, 1,2,3,4,5,8,7,6,9,10,11)
# print(x)
