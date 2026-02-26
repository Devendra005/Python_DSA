nums = [55,32,-97,99,3,67]
largest = float("-inf")
n = len(nums)
for i in range (0,n):
    largest = max(largest,nums[i])
print(largest)