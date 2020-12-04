# https://skillsmart.ru/algo/lvl1/f8c6.html

def MisterRobot(*args):
    if isinstance(args[1], int):
        data = list(args[1:])
    else:
        data = args[1]

    checked = []
    while True:
        if data != sorted(data):
            for i in range(len(data)-3):
                c = data[i:i+3]
                if sorted(c) != c:
                    for k in range(3):
                        try:
                            ch = [c[k], c[k-2], c[k-1]]
                        except IndexError:
                            break
                        if ch == sorted(c):
                            data[i:i+3] = ch
                            break
            if data in checked and data != sorted(data):
                return False
            checked.append(data)
        else:
            return True

#
# x = MisterRobot(7, [1,4,3,5,7,6,2])
# x = MisterRobot(7, [1,3,4,5,6,2,7])
# print(x)
