nums = [5,9,3]
result = []

def find_subsequences(index, subset):
    if index >= len(nums):
        result.append(subset.copy())
        return
    subset.append(nums[index])
    find_subsequences(index + 1, subset)
    subset.pop()
    find_subsequences(index + 1, subset)
find_subsequences(0, [])
print(result)