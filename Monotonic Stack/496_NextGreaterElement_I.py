nums1 = [4,1,2] 
nums2 = [1,3,4,2]

def NextGreaterElem(nums1, nums2):
    stack = []
    nge = {}

    for num in nums2:
        while stack and stack[-1] < num:
            nge[stack.pop()] = num
        stack.append(num)

    while stack:
        nge[stack.pop()] = -1
        
    return[nge[num] for num in nums1]

print(NextGreaterElem(nums1, nums2))