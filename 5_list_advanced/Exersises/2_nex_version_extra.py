version = [int(digit) for digit in input().split(".")]
version[-1] += 1

for ind in range(len(version)-1,0,-1):
    if version[ind] > 9:
        version[ind] = 0
        version[ind-1] += 1

print(".".join(str(digit) for digit in version))


