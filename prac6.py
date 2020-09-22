
horizvert = {

            1:[6,9,2],
            2:[1,3,8,5],
            3:[4,7,2],
            4:[5,3],
            5:[2,6,4],
            6:[1,5],
            7:[8,3],
            8:[2,7,9],
            9:[1,8]

             }

diagonals = {

            1:[8,5],
            2:[6,9,7,4],
            3:[8,5],
            4:[2],
            5:[1,3],
            6:[2],
            7:[2],
            8:[1,3],
            9:[2]

            }

def PatternUnlock(*args):
    if args[0] <= 1:
        return 0

    if type(args[1]) == int:
        hints = args[1:]
    elif type(args[1]) == list or type(args[1]) == tuple:
        hints = args[1]

    length = 0
    horiz = 1
    vert = (horiz + horiz) ** 0.5 # длина диагонали

    for i in range(len(hints)):
        try:
            i_next = hints[i+1]
        except IndexError:
            break
        if hints[i] == 6 and i_next == 7:
            length += vert * 2
        elif i_next in horizvert[hints[i]]:
            length += horiz
        else:
            length += vert

    length = round(length, 5)


    str_len = str(length)
    str_len = str_len.replace('0', '')
    str_len = str_len.replace('.', '')

    return str_len
#
#
