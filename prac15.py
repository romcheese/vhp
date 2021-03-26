
def TankRush(H1,W1,S1,H2,W2,S2):
    arr1 = S1.split()
    arr2 = S2.split()
    check_arr = list()
    i = 0
    z = 0
    try:
        while True:
            x = arr1[i].find(arr2[0], z)
            if x != -1:
                for y in range(H2):
                    f = arr1[i+y][x:x+W2]
                    check_arr.append(str(f))
                if check_arr == arr2:
                    return True
                else:
                    check_arr.clear()
                    z = x+1
            else:
                i+= 1
                z = 0
    except IndexError:
        return False



# x = TankRush(3,4,'1234 5678 9102', 2,2,'56 91')
# x = TankRush(3,4,'1245 2355 0987',2,2,'55 77')
# x =TankRush(3,3, '321 694 798', 2, 2, '69 98') #= false
# x = TankRush(3,3, '991 999 798', 2, 2, '99 79')
# print(x)
