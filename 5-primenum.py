from functools import reduce

def checker(num):
    units = []
    while num > 0:
        unit = num % 10
        units.append(unit)
        num //= 10

    units = units[::-1]
    poss = []
    primes = 0

    for i in range(len(units)):
        tmp = units[i::] + units[:i]
        number = reduce(lambda a, b: a*10 + b, tmp)
        poss.extend([number])

    print(poss)
    for item in poss:
        flag = False
        for i in range(2, item):
            if (item % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        if not flag:
            primes += 1

    return len(poss) == primes

n = 2
res = []

while n < 1000:
    result = checker(n)
    if result:
        res.append(n)
    n += 1

print(res)
