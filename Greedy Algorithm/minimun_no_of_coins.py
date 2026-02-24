def min_coins(self, N):
    coins = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    
    i = 0
    result = []
    total = N
    
    while total > 0:
        if total >= coins[i]:
            result.append(coins[i])
            total -= coins[i]
        else:
            i += 1
    return result

N = 47
print(min_coins(0,N))