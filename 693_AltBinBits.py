n = 7

def AltBin(n):
    A = n ^ (n >> 1)
    return (A & (A + 1)) == 0

print(AltBin(n))