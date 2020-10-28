# int [] UFO(int N, int [] data, bool octal)
# https://skillsmart.ru/algo/lvl1/3b3d.html

def UFO(*args):
    
    octal = args[-1]

    if type(args[1]) == int:
        nums = args[1:-1]
    else:
        nums = args[1]

    sum = 0
    result = []

    for num in nums:
        num = str(num)[::-1]
        for i in range(len(num)):
            if octal == False:
                x = int(num[i])*16**i
            else:
                x = int(num[i])*8**i
            sum += x
        result.append(sum)
        sum = 0

    return result
