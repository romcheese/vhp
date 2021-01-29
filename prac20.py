cache = ['']
redo_cache = []
def BastShoe(str:str):
    global cache
    global redo_cache
    # не знаю, как сделать экранирование переменной
    act = str[0]
    p = str[2:]
    try:
        if int(act) not in range(1, 6): # проверка на корр акта
            return cache[-1]
    except ValueError:
        return ''

    if act == '1' or act == '2':
        x = cache[-1]
        if act == '1':
            x += p
        elif act == '2':
            if len(x) <= int(p):
                x = ''
            else:
                x = x[:-int(p)]
        cache.append(x)

        if len(redo_cache) != 0: # если были операции 1,2 после undo
            cache = cache[-2:]
            redo_cache.clear()

        return cache[-1]

    elif act == '3':
        try:
            p = int(p)
        except ValueError:
            return ''
        try:
            return cache[-1][p]
        except IndexError:
            return ''

    elif act == '4':
        if len(cache) >= 2:
            x = cache.pop()
            redo_cache.append(x)
        return cache[-1]

    elif act == '5':
        if len(redo_cache) != 0:
            x = redo_cache.pop()
            cache.append(x)
        return cache[-1]


# #
# # 1 Привет
# # В текущей строке будет "Привет"
# # 1  , Мир!
# # Привет, Мир!
# # 1 ++
# # Привет, Мир!++
# # 2 2
# # Привет, Мир!
# # 4
# # Привет, Мир!++
# # 4
# # Привет, Мир!
# # 1 *
# # Привет, Мир!*
# # 4
# # Привет, Мир!
# # 4
# # Привет, Мир!
# # 4
# z = '1 Привет'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 , Мир!'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 ++'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '2 2'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 *'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '3 6'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '2 100'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 Привет'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 , Мир!'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '1 ++'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '2 2'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '4'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
# z = '5'
# x = BastShoe(z)
# print(z)
# print(x)
    # здесь вставляем проверку на корректность
    # if act == '1' or act == '2':
    #     x = cache.pop()
    #     cache.append()
    #
    #     if act == '1':
    #         x += p
    #
    #     elif act == '2':
    #         x = x[:-int(p)]
    #
    #     if len(redo_cache) != 0:
    #         cache = cache[-1, x]
    #         redo_cache = []
    #     else:
    #         cache.append(x)
    #
    #     return cache[-1]
    #
    # elif act == '3': #undo
    #     x = cache.pop()
    #     redo_cache.append(x)
    #     return cache[-1]
    #
    # elif act == '4': #redo
    #     try:
    #         return redo_cache.pop()
    #     except IndexError:
    #         return ''

# if int(act) not in range(1,6):
#     return current_s
# if act == '1': #add
#     current_s += w
# elif act == '2': #delete from end
#     if len(s) <= int(act):
#         current_s = ''
#         return current_s
#     else:
#         current_s = current_s[:int(-act)]
#         return current_s
