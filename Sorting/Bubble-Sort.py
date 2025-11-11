# Bubble Sort
# Compares adjacent elements, swaps if element to right is bigger than element to left
# Complexity = O(n^2) - Since 2 for loops are present

arr = [5,2,8,1,9,4,7,6]

def BubbleSort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


print(BubbleSort(arr))
