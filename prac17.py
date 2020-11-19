# https://skillsmart.ru/algo/lvl1/d146.html
# *..*...*..*..*..*..*
# *..*..*..*..*..**..*
# correct:
# * - exception
# ***
# *.......*.......*
# **
# *.*

def LineAnalysis(s):
    if s.startswith('*') != True or s.endswith('*') != True:
        return False
    check = True

    for elem in s:
        if elem != '*':
            check = False
            break

    if check == True:
        return True

    z = 0
    e = len(s) - 1
    while True:
        i = s.find('*', z)
        if i == -1 or i == e:
            break
        else:
            if s[i+1] == '*':
                return False
            z = i + 1

    s = s.strip('*')
    s = s.split('*')

    for elem in s:
        if elem != s[0]:
            return False
    return True
