check = False
def BalancedParentheses(N):
    global check
    if check == False: # первый заход
        global z
        global elems
        z = N
        x = '('+'()'*(N-1)+')'
        elems = [x]
        check = True

    if N == 0:
        check = False
        return ' '.join(elems)
    else:
        base = '()'*(z-N)+'('*(N-1)+')'*(N-1)

        for i in range(z*2):
            a = base[:i]+'()'+base[i:]
            b = '' # зеркало
            for letter in a[::-1]:
                if letter == '(':
                    b += ')'
                else:
                    b += '('
            if a not in elems:
                elems.append(a)
            if b not in elems:
                elems.append(b)

        return BalancedParentheses(N-1)
