# https://skillsmart.ru/algo/lvl1/f8c6.html

def MisterRobot(*args):
    if isinstance(args[1], int):
        data = list(args[1:])
    else:
        data = args[1]

    checked = []
    while True:
        if data != sorted(data):
            if data not in checked:
                for i in range(len(data)):
                    c = data[i:i+3]
                    if sorted(c) != c:
                        checked.append(data)
                        for k in range(3):
                            ch = [c[k], c[k-2], c[k-1]]
                            if ch == sorted(c):
                                data[i:i+3] = ch
                                break
            else:
                return False
        else:
            return True

# 
# x = MisterRobot(7, [1,3,4,5,2,6,7])
# print(x)
