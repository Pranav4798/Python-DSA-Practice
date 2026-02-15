nums = [8,1,2,2,3]


def SmallerCurrent(nums):
    
    N = len(nums)
    G = 0
    L = []

    for i in range(0, N):
        for j in range(0, N):
            if nums[i] > nums[j]:
                G += 1
        L.append(G)
        G = 0
    return L

print(SmallerCurrent(nums))       