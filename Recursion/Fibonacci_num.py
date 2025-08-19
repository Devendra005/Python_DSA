def func(nums):
    if nums == 0 or nums == 1:
        return nums
    return func(nums-1)+ func(nums-2)
num = int(input("Enter number : "))
print(func(num))