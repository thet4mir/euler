plist = [1,2]
for i in range(3,10):
    res = 1
    for j in range(1,i+1):
        res *= j

    plist.append(res)

print(plist)

def checker(num):
    sum = 0
    while num > 0:
        unit = num % 10
        if unit != 0:
            sum += plist[unit - 1]
        num //= 10
    return sum

n = 0
res = []
while n < 1000000:
    sum = checker(n)
    if sum == n:
        res.append(n)
    n += 1

print(res)
