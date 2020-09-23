# n >= 2
def SumOfThe(*args):
    n = args[0]

    if type(args[1]) == int:
        nums = list(args[1:])

    elif type(args[1]) == tuple or type(args[1]) == list:
        nums = list(args[1])


    for i in range(len(nums)):
        num = nums.pop(i)
        if num == sum(nums):
            return num
        else:
            nums.append(num)
