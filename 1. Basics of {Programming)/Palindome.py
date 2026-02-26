# check if the string is palindrome or not using recursion/loop

#Using while loop
s = "ANBCDDCBNA"
n = len(s)
left = 0
right = n-1
while left < right:
    if s[left] != s[right]:
        print("False")
        break
    left +=1
    right -=1
else:
    print("True")
    

#Using recursion
def func(s,left,right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s,left+1,right-1)
print(func(s,0,n-1))