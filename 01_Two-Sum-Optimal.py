nums = [2,8,1,3,6,9,4]
T = 11

def TwoSum(nums, T):
    OP = {}

    for i, n in enumerate(nums):
        P = T - n

        if P in OP:
            return [OP[P], n]
        
        OP[n] = i

print(TwoSum(nums, T))