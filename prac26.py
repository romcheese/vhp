elems = []
check = False
def BalancedParentheses(N):
    global elems
    global check

    if check == False:
        c = N
        z = N
        check = True
        x = '('*(N-1)+')'*(N-1)
        y = '()'*(N-1)
        elems.append(x)
        elems.append(y)

    if N < -2:
        ### здесь надо удалить первые два элемента из elems
        return ' '.join(elems[2:])
    try:
        for i in range(2):
            el_o, el_t = list(elems[i]), list(elems[i])
            el_o.insert(N, '()')
            el_t.insert(N*2, '()')
            el_o = ''.join(el_o)
            el_t = ''.join(el_t)
            if el_o not in elems:
                elems.append(el_o)
            if el_t not in elems:
                elems.append(el_t)
    except IndexError:
        return '()'


    return BalancedParentheses(N-1)
# 
#
# x = BalancedParentheses(3)
# print(x)
