# Selection sort

arr = [25, 11, 78, 91, 7, 21, 84]

def SelectSort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a

print(SelectSort(arr))