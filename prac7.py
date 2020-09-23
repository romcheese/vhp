#https://skillsmart.ru/algo/lvl1/6d4d.html
def WordSearch(leng, string, subs):

    words = string.split()

    lines = dict()
    i = 0
    lines[i] = ''

    for word in words:
        if len(word) <= leng:
            temp_str = lines[i] +  ' ' + word
            temp_str = temp_str.strip()
            if len(temp_str) <= leng:
                lines[i] = temp_str
                continue
            elif len(temp_str) > leng:
                lines[i+1] = word
                i+=1
                continue

        elif len(word) > leng: # сюда подставить word, потом распиливаем
            l = 0
            while True: # распил
                part = word[:leng]
                l = l + len(part)
                lines[i] = part
                if l >= len(word):
                    break
                else:
                    i += 1
                    word = word[leng:]

    zeroes_ones = []
    for k in range(len(lines)):
        words = lines[k]
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.split()
        if subs in words:
            zeroes_ones.append(1)
        else:
            zeroes_ones.append(0)
            
    return zeroes_ones
