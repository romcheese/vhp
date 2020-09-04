def squirrel(n:int):
    number = 1
    for i in range(number, n+1):
        number = i * number
    return int(str(number)[0])
