nums = [[5,10,8],[7,6,3],[2,1,9]]
rows = len(nums)
cols =len(nums[0])

#Upper Triangle
for i in range(0,rows):
    for j in range(0,cols):
        if j>=i:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()


# Lower Triangle
for i in range(0,rows):
    for j in range(0,cols):
        if i>=j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()


#diagonal elements 
for i in range(0,rows):
    for j in range(0,cols):
        if i == j:
            print(nums[i][j],end=" ")
        else:
            print("*",end=" ")
    print()
print()


#transpose
result = [[0]*rows for _ in range(cols)]
for i in range(0,rows):
    for j in range(0,cols):
        result[j][i]=nums[i][j]
print(result)