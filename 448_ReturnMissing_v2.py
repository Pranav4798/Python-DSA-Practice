nums = [4,3,2,7,8,2,3,1]


def ReturnMiss(nums):

    N = len(nums)

    N_set = set(nums)
    M = [i for i in range(1, N+1) if i not in N_set]
    return M

print(ReturnMiss(nums))



