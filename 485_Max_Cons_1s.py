nums = [1,1,0,1,1,1]

def maxCons(nums):
    C = 0
    maxC = 0

    for i in nums:
        if i == 1:
            C += 1
            if C > maxC:
                maxC = C
        else:
            C = 0

    return maxC

print(maxCons(nums))
    