nums = [1,99,101,98,2,5,3,100,1,1,1]
n = len(nums)
my_set = set()
for i in range(0,n):
    my_set.add(nums[i])
longest = 0
for num in my_set:
    if num-1 not in my_set:
        x = num
        count = 1
        while x + 1 in my_set:
            count += 1
            x += 1
        longest = max(longest,count)
print(longest)