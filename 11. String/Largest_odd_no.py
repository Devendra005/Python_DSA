num = "6783842"

n = len(num)
for i in range(n-1, -1, -1):
    if int(num[i])%2 == 1:
        print(num[0:i+1])
        break
        exit()
print("")
