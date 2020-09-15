# https://skillsmart.ru/algo/lvl1/z3b8.html

# int, int
# int, list
# list, list
# list, int

def SynchronizingTables(*args):

    n = args[0]

    if type(args[1]) == int:
        ids = args[1:n+1]
        if type(args[n+1]) == int: # int-int
            salary = args[n+1:]
        else:
            salary = args[n+1] # int-list

    elif type(args[1]) == list or type(args[1]) == tuple:
        ids = args[1]
        if type(args[2]) == list or type(args[2]) == tuple: # list-list
            salary = args[2]
        else: # list-int
            salary = args[2:]

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
