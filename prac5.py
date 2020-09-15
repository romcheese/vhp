# https://skillsmart.ru/algo/lvl1/z3b8.html
def SynchronizingTables(*args):

    n = args[0]
    ids = args[1]
    salary = args[2]

    s_ids = sorted(ids)
    s_salary = sorted(salary)

    d = dict()

    for i in range(len(ids)):
        d[s_ids[i]] = s_salary[i]

    salary_lst = list()

    for i in ids:
        x = d[i]
        salary_lst.append(x)

    return salary_lst
