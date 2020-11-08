# https://skillsmart.ru/algo/lvl1/off8.html
def TankRush(H1,W1,S1,H2,W2,S2):
    S1 = S1.split()
    S2 = S2.split()
    res = []

    for elem1 in S1:
        for elem2 in S2:
            if elem2 in elem1:
                res.append(True)
                break
    if len(res) == H2:
        return True
    else:
        return False
