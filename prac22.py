# https://skillsmart.ru/algo/lvl1/b7de.html

def SherlockValidString(s:str):
    letters = []

    for letter in s:
        letters.append(letter)

    set_l = set(letters)

    d_letters = {}

    for letter in set_l:
        d_letters[letter] = s.count(letter)

    values = list(d_letters.values())
    mx = max(values)
    mn = min(values)
    s_values = list(set(values)) 

    if len(set(values)) == 1:
        return True
    elif len(set(values)) > 2:
        return False
    elif len(set(values)) == 2:
        count = 0
        if mx - mn != 1:
            return False
        else:
            biggest = 0
            for val in s_values:
                if values.count(val) > biggest:
                    biggest = val
            base = biggest

            for value in values:
                if base - value != 0:
                    count += 1
            if count > 1:
                return False
            else:
                return True
