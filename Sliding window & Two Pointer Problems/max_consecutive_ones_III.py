nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]

def longestOnes(self, nums: list[int], k: int) -> int:
    left = 0
    right = 0
    zeros = 0
    n = len(nums)
    max_lenght = 0
    while right < n:
        if nums[right] == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        if zeros <= k:
            lenght = right - left + 1
            max_lenght = max(max_lenght, lenght)
        right += 1
    return max_lenght

print(longestOnes(0, nums, 2))