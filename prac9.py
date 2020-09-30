# s = 'отдай мою кроличью лапку'
# s = 'омоюу толл дюиа акчп йрьк...'
# https://skillsmart.ru/algo/lvl1/ab53.html

def TheRabbitsFoot(s, encode: bool):
    if encode == True:
        s = s.replace(' ', '')
        l = len(s)**0.5
        lb = len(s) // l # lower border
        ub = lb + 1 # upper border
        l2 = len(s) # длина слов без пробелов

        while True: # создание матрицы
            result = lb * ub
            if result < len(s):
                lb += 1
            else:
                break

            phrase = []
            count = 0
            while True:
                slice = s[:int(ub)]
                count = count + len(slice)
                phrase.append(slice)
                if count >= l2:
                    break
                else:
                    s = s[int(ub):]
            st = ''


            for i in range(int(lb)): # encode
                for word in phrase:
                    try:
                        x = word[i]
                        st += str(x)
                    except IndexError:
                        break
                st += ' ' # correct before here
            return st
    elif encode == False:
        s = s.replace('.', '')
        s = s.split()
        # biggest i
        biggest_i = 0
        decode = ''

        for word in s:
            i = len(word)
            if i > biggest_i:
                biggest_i = i


        for i in range(biggest_i):
            for word in s:
                try:
                    decode += word[i]
                except IndexError:
                    return decode

#
#
#
#
#
# #
# x = TheRabbitsFoot(s, False)
# print(x)
