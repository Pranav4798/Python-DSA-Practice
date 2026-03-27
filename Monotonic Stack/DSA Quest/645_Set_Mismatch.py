nums = [1,2,2,4]


def SetMis(nums):
    n = len(nums)
    counts = {}
    dup = -1
    miss = -1

    for x in nums:
        if x in counts:
            dup = x
        counts[x] = 1

    for i in range(1, n+1):
        if i not in counts:
            miss = i
    return dup, miss

print(SetMis(nums))