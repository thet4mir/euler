target = 200
coins = [1,2,5,10,20,50,100]
result = [0]

def combinations(target, coins):
    def backtracking(curr,idx):
        s = sum(curr)

        if s == target:
            result[0] += 1
        elif s < target:
            for j in range(idx,len(coins)):
                backtracking(curr + [coins[j]], j)

    backtracking([], 0)
    return result[0]

res = combinations(target, coins)
print(res)
