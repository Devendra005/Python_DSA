nums = [5,1,1,9,2,10]
k = 9
result = []

def backtract(index, total, subset):
    if total == k:
        result.append(subset.copy())
        return True
    elif total > k:
        return False
    if index >= len(nums):
        return False
    subset.append(nums[index])
    Sum = total + nums[index]
    pick = backtract(index + 1, Sum, subset)
    if pick == True:
        return True
    subset.pop()
    not_pick = backtract(index + 1, total, subset)
    return False
print(backtract(0, 0, []))
print("Subsequence with sum =", k, "is:", result)
