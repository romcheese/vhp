elems = []
check = False
def BalancedParentheses(N):
    global elems
    global check
    global z

    if check == False:

        z = N
        check = True
        x = '('*(N-1)+')'*(N-1)
        y = '()'*(N-1)
        h = '('+(N-1)*'()'+')'
        elems.append(x)
        elems.append(y)
        elems.append(h)

    if N < -1:
        ### здесь надо удалить первые два элемента из elems
        return ' '.join(elems[2:])

    for i in range(2):
        a = elems[i][:N]+'()'+elems[i][N:]
        b = ''
        for elem in a[::-1]:
            if elem == '(':
                b+= ')'
            else:
                b+= '('
        if a not in elems:
            elems.append(a)
        elif b not in elems:
            elems.append(b)

    return BalancedParentheses(N-1)
#
#
# x = BalancedParentheses(1)
# print(len(x))
