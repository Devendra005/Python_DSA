nums = [5,9,3,4,1]
result = []
target = 9

def sum_of_k_subsequences(index, total, subset):
    if total == target:
        result.append(subset.copy())
        return
    if index >= len(nums):
        return
    if total > target:
        return
    subset.append(nums[index])
    new_total = total + nums[index]
    sum_of_k_subsequences(index + 1, new_total, subset)
    subset.pop()
    sum_of_k_subsequences(index + 1, total, subset)
    return

sum_of_k_subsequences(0, 0, [])
print(result)