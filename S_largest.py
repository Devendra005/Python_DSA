nums = [55,32,97,-55,45,32,88,21]
largest = float("-inf")
s_largest = float("-inf")
n = len(nums)
for i in range (0,n):
    largest = max(largest,nums[i])
for i in range(0,n):
    if nums[i]>s_largest and nums[i]!=largest:
        s_largest = nums[i]
print(s_largest)