# https://skillsmart.ru/algo/lvl1/off8.html
def TankRush(H1,W1,S1,H2,W2,S2):
    S1 = S1.split()
    S2 = S2.split()
    res = []
    i = 0
    for elem2 in S2:
        for elem1 in S1:
            if elem2 in elem1:
                res.append(True)
                break
            i+= 1
    if len(res) == H2:
        return True
    else:
        return False

# x = TankRush(3,4,'1234 5678 9102', 2,2,'34 78')
# x = TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98')
# print(x)
