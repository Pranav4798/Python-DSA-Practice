n = 43261596

def RevBits(n):

    res = 0
    for i in range(32):
        res = res << 1
        res = res | (n & 1)
        n = n >> 1

    return res


print(RevBits(n))