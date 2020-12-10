# https://skillsmart.ru/algo/lvl1/b519.html
# не рассматриваем вариант, где на входе на args[1] - строка
def ShopOLAP(*args):
    items = args[1]
    d_items = dict()

    for item in items:
        item = item.split()
        if item[0] in d_items:
            d_items[item[0]] += int(item[1])
        else:
            d_items[item[0]] = int(item[1])

    s_keys = sorted(d_items.keys()) # сортируем словарь на названию
    sd_items = {}
    for item in s_keys:
        sd_items[item] = d_items[item]
    # sd_items - отсортированный по назв словарь покупок

    m = max(sd_items.values())
    result = []
    while m != -1:
        for k, v in sd_items.items():
            if v == m:
                x = f'{k} {v}'
                result.append(x)
                sd_items[k] = -1
        m = max(sd_items.values())
    return result
#
# x = ['платье1 5',
# 'сумка32 2',
# 'платье1 1',
# 'сумка23 2',
# 'сумка128 4']
#
# y = ShopOLAP(1, x)
