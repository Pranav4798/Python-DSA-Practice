a = [2,5,1,3,4,7]
n = 3
result = []

for i in range(n):
    result.append(a[i])
    result.append(a[i+n])

print(result)