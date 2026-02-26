prices = [7,2,1,5,6,4,8]

n = len(prices)
max_profit = 0
for i in range(0,n):
    for j in range(i+1,n):
        if prices[j]>prices[i]:
            p = prices[j]-prices[i]
            max_profit = max(max_profit,p)
print(max_profit)

#optimal solution 

min_price = float("inf")
for i in range(0,n):
    min_price = min(min_price,prices[i])
    max_profit = max(max_profit,prices[i]-min_price)
print(max_profit)