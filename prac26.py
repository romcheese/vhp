z = 0
def BalancedParentheses(N):
    global z
    z += N
    if z == N:
        x = BalancedParentheses(N-1)
        return ' '.join(x)
    else:
        p = '()'
        x = '('*N+')'*N
        y = p*N
        x, y = list(x), list(y)
        elems = []
        for i in range(len(x)+1):
            x.insert(i, p)
            y.insert(i, p)
            elem_x = ''.join(x)
            elem_y = ''.join(y)
            if elem_y not in elems:
                elems.append(''.join(elem_y))
            if elem_x not in elems:
                elems.append(''.join(elem_x))
            x.pop(i)
            y.pop(i)
        return elems
#
# x = BalancedParentheses(2)
# # print(type(x))
# print(x)
