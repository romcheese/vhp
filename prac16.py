# https://skillsmart.ru/algo/lvl1/beea.html
# 400, 350, 300, 250, 200,150 ,100
# int MaximumDiscount(int N, int [] price)
def MaximumDiscount(*args):
    n = args[0]

    if type(args[1]) == int:
        price = args[1:]
    else:
        price = args[1]

    if len(price) < 3:
        return 0

    price = sorted(price)[::-1]

    z = 2
    i = 0
    discount = 0
    x = n//3

    while i != x:
        discount += price[z]
        z += 3
        i += 1

    return discount
#
# x = MaximumDiscount(7, [400, 400, 400, 400, 350, 100 ,150])
#
# print(x)
