nums = [1,3,2,1]
k = 4

def count_subsequences(index, total):
    if total == k:
        return 1
    if index >= len(nums):
        return 0
    if total > k:
        return 0
    Sum = total + nums[index]
    pick = count_subsequences(index + 1, Sum)
    Sum = total
    not_pick = count_subsequences(index + 1, total)
    return pick + not_pick
print(count_subsequences(0, 0))